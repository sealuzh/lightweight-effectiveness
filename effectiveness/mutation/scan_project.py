__author__ = "Giovanni Grano"
__license__ = "MIT"
__email__ = "grano@ifi.uzh.ch"

from effectiveness.mutation.utils import *
from effectiveness.mutation.get_commit import *
from collections import OrderedDict
from effectiveness.settings import *
import subprocess
import logging

import xml.etree.ElementTree as ET
import os
import pandas as pd


special_cases = {'core': ['/src/', '/test/'],
                 'guava': ['/src/', '/guava-tests/test/'],
                 'guava-gwt': ['/src/', '/test/']}


def get_submodules(project_path):
    """
      Analyzes the structure of the project and detect whether more modules are present
      :param project_path the path of the project
      :return: a list of modules
      """
    pom_path = project_path + '/pom.xml'
    assert(os.path.exists(pom_path))
    pom_file = open(pom_path)
    pom_content = pom_file.read()
    pom_content = re.sub(r'\sxmlns="[^"]+"', '', pom_content, count=1)
    pom_parsed = ET.fromstring(pom_content)
    modules = pom_parsed.findall('modules')
    modules_list = []
    if modules:
        for module in modules[0].findall('module'):
            detected_module = module.text
            if not 'xml' in detected_module:
                modules_list.append(detected_module)
    logging.info('Found {} module:\n'
                 '{}'.format(len(modules_list), modules_list))
    pom_file.close()
    return modules_list


def has_submodules(project_path):
    """
    Checks whether the project has submodules
    :param project_path the path of the project
    :return: a boolean value
    """
    pom_path = project_path + '/pom.xml'
    assert(os.path.exists(pom_path))
    pom_file = open(pom_path)
    pom_content = pom_file.read()
    pom_content = re.sub(r'\sxmlns="[^"]+"', '', pom_content, count=1)
    pom_parsed = ET.fromstring(pom_content)
    modules = pom_parsed.findall('modules')
    pom_file.close()
    if modules:
        true_modules = 0
        for module in modules[0].findall('module'):
            detected_module = module.text
            if not 'xml' in detected_module:
                true_modules += 1
        if true_modules > 0:
            logging.info('Submodules found')
            return True
    logging.info('No submodules found')
    return False


def get_test_and_classes(project_path,
                         project_name,
                         module_name=None,
                         save=False,
                         path_to_save=RESULTS_DIR,
                         source_directory=None,
                         test_directory=None):
    """
    Scan a project and return the pairs of classes and tests; it might save of not to a file

    :param project_path: the path for the project
    :param project_name: the name of the project
    :param module_name: the name of the module
    :param save: flag for saving on a file or no (it has to be false while working with submodules)
    :param path_to_save: the output path
    :param source_directory: the directory that contains the source code
    :param test_directory: the directory that contains the test code
    :return: a list of Projects or False, where it was not possible to detect the pom
    """
    name = os.path.basename(project_path)

    loc = os.path.join(project_path, 'pom.xml')
    if not os.path.exists(loc):
        convert = subprocess.run('mvn one:convert'.split(),
                                 cwd=project_path,
                                 stderr=subprocess.PIPE)
        if convert.returncode == 0:
            print('Conversion done')
        else:
            print('Conversion failed')
            return False

    tree = ET.parse(loc)
    root = tree.getroot()

    include_pattern = []
    exclude_pattern = []

    source_directory, test_source_directory = get_source_directories(proj_path=project_path,
                                                                     project_name=project_name,
                                                                     module_name=module_name)

    for plugin in root.findall('*//{http://maven.apache.org/POM/4.0.0}plugin'):
        flag = False
        for tag in plugin.getiterator():
            if tag.tag.strip() == '{http://maven.apache.org/POM/4.0.0}artifactId' and tag.text.strip() \
                    == 'maven-surefire-plugin':
                flag = True
            if flag and tag.tag.strip() == '{http://maven.apache.org/POM/4.0.0}include':
                include_pattern.append(tag.text)
            if flag and tag.tag.strip() == '{http://maven.apache.org/POM/4.0.0}exclude':
                exclude_pattern.append(tag.text)

    if not include_pattern and not project_name == 'joda-beans':
        include_pattern.append('**/*Test.java')
    elif project_name == 'joda-beans':  # particular case of joda-beans
        include_pattern.append('**/Test*.java')
    elif module_name == 'guava-gwt':
        include_pattern.append('**/Test_gwt.java')

    project = Project(name, include_pattern, exclude_pattern, project_path)
    # special case for guava
    if project_name == 'guava' and not project_path.endswith('gwt'):
        tests_path = os.path.dirname(project_path) + test_source_directory
    else:
        tests_path = project_path + test_source_directory
    main_path = project_path + source_directory
    lst = project.get_tests(tests_path, main_path)
    if save:
        if not module_name:
            csv_out(lst, project_path, project,
                    project_name=project_name,
                    output=path_to_save)
        else:
            csv_out(lst, os.path.dirname(project_path), project,
                    project_name=project_name,
                    output=path_to_save,
                    module_name=module_name)
    return lst


def get_source_directories(proj_path, project_name, module_name=None):
    """Return the source and test source directory from the pom (or one of the pom)

    Arguments
    -------------
    - proj_path: the path for the project

    """
    look_for = project_name if not module_name else module_name
    if look_for in special_cases.keys():
        return special_cases[look_for][0], special_cases[look_for][1]

    pom_paths = []
    for file in os.listdir(proj_path):
        if file.startswith('pom'):
            pom_paths.append(os.path.join(proj_path, file))
    aux_source = look_for_tag_only_under_build(pom_paths, 'sourceDirectory')
    aux_test = look_for_tag_only_under_build(pom_paths, 'testSourceDirectory')

    # check che test dir and the source dir
    test_dir = '/src/test/java/' if aux_test is None else aux_test
    test_dir = fix_path(test_dir)

    src_dir = '/src/main/' if aux_source is None else aux_source
    src_dir = fix_path(src_dir)

    return src_dir, test_dir


def fix_path(path):
    """
    Fixes the path with the slashes in front and at the bottom, if they are not there
    :param path: the path to check
    :return: the correct path
    """
    correct_path = '/' + path if not path.startswith('/') else path
    correct_path = correct_path + '/' if not correct_path.endswith('/') else correct_path
    return correct_path


def look_for_tag(list_files, tag):
    """Looks for a given tag into a set of poms

    Arguments
    -------------
    - list_files: the list of poms given
    - tag: the tag to look for

    """
    for detected_pom in list_files:
        tree = ET.parse(detected_pom)
        root = tree.getroot()
        pattern = '*//{http://maven.apache.org/POM/4.0.0}' + tag
        for match in root.findall(pattern):
            matched = match.text
            matched = re.sub("[$@*}?].*[$@*}?]", "", matched)
            return matched


def look_for_tag_only_under_build(list_files, tag):
    """Looks for a given tag into a set of poms. Only looks at the child of the <build> tag

    Arguments
    -------------
    - list_files: the list of poms given
    - tag: the tag to look for

    """
    for detected_pom in list_files:
        with open(detected_pom) as f:
            xmlstring = f.read()
        xmlstring = re.sub(r'\sxmlns="[^"]+"', '', xmlstring, count=1)

        pom = ET.fromstring(xmlstring)
        matches = pom.findall("build")
        if matches:
            pattern = tag
            for match in matches[0].findall(pattern):
                matched = match.text
                matched = re.sub("[$@*}?].*[$@*}?]", "", matched)
                return matched


def csv_out(lst, project_path, project, project_name, output=RESULTS_DIR, module_name=None):
    """It saves the output of a project scanning to file

    Arguments
    -------------
    - list_files: the list of poms given
    - tag: the tag to look for
    - project_path: the path for the main project folder
    - project: the Project object that contains the list of the pairs
    - output: the directory for the output
    - module_name: the eventual name of the module under analysis

    """ 
    last_commit = get_last_commit_id(project_path)
    projects = [project_name for x in lst]
    commit = [last_commit for x in lst]
    module = [module_name for x in lst]
    path_test = [x.get_test_path() for x in lst]
    test_name = [x.get_qualified_test_name() for x in lst]
    path_src = [x.get_source_path() for x in lst]
    src_name = [x.get_qualified_source_name() for x in lst]
    frame = pd.DataFrame(OrderedDict((('project', projects),
                                      ('module', module),
                                      ('commit', commit),
                                      ('path_test', path_test),
                                      ('test_name', test_name),
                                      ('path_src', path_src),
                                      ('class_name', src_name))))
    output = '{}/res_'.format(output)+project.get_project_name()+'.csv'
    frame.to_csv(output, index=False)


if __name__ == '__main__':
    projects = ['cat']

    for project in projects:
        project_path = os.path.join(PROJECTS, project)
        get_test_and_classes(project_path=project_path, project_name=project, save=True)
