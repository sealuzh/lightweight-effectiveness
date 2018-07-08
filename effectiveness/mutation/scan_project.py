__author__ = "Giovanni Grano"
__license__ = "MIT"
__email__ = "grano@ifi.uzh.ch"

from effectiveness.mutation.utils import *
from effectiveness.mutation.get_commit import *
from collections import OrderedDict
from effectiveness.settings import *
import subprocess

import xml.etree.ElementTree as ET
import os
import pandas as pd


def get_test_and_classes(proj_path, save=True, path_to_save=RESULTS_DIR):
    """
    Scan a project and return the pairs of classes and tests; it might save of not to a file

    :param proj_path:  the path for the project
    :param save: flag for saving on a file or no
    :param path_to_save: the output path
    :return: a list of Projects or False, where it was not possible to detect the pom
    """
    name = os.path.basename(proj_path)

    loc = os.path.join(proj_path, 'pom.xml')
    if not os.path.exists(loc):
        convert = subprocess.run('mvn one:convert'.split(),
                                 cwd=proj_path,
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

    source_directory, test_source_directory = get_source_directories(proj_path)

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

    if not include_pattern and not proj_path == 'joda-beans':
        include_pattern.append('**/*Test.java')
    elif proj_path == 'joda-beans':  # particular case of joda-beans
        include_pattern.append('**/Test*.java')

    project = Project(name, include_pattern, exclude_pattern, proj_path)
    tests_path = proj_path + test_source_directory
    main_path = proj_path + source_directory
    lst = project.get_tests(tests_path, main_path)
    if save:
        csv_out(lst, project, path_to_save)
    return lst


def get_source_directories(proj_path):
    """Return the source and test source directory from the pom (or one of the pom)

    Arguments
    -------------
    - proj_path: the path for the project

    """
    pom_paths = []
    for file in os.listdir(proj_path):
        if file.startswith('pom'):
            pom_paths.append(os.path.join(proj_path, file))
    aux_source = look_for_tag_only_under_build(pom_paths, 'sourceDirectory')
    aux_test = look_for_tag_only_under_build(pom_paths, 'testSourceDirectory')

    # check che test dir and the source dir
    test_dir = '/src/test/java/' if aux_test is None else aux_test
    test_dir = '/' + test_dir if not test_dir.startswith('/') else test_dir
    test_dir = test_dir + '/' if not test_dir.endswith('/') else test_dir

    #
    src_dir = '/src/main/' if aux_source is None else aux_source
    src_dir = '/' + src_dir if not src_dir.startswith('/') else src_dir
    src_dir = src_dir + '/' if not src_dir.endswith('/') else src_dir

    return src_dir, test_dir


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


def csv_out(lst, project, output=RESULTS_DIR):
    """It saves the output of a project scanning to file

    Arguments
    -------------
    - list_files: the list of poms given
    - tag: the tag to look for

    """ 
    last_commit = get_last_commit_id(project.get_project_path())
    projects = [x.get_project() for x in lst]
    commit = [last_commit for x in lst]
    path_test = [x.get_test_path() for x in lst]
    test_name = [x.get_qualified_test_name() for x in lst]
    path_src = [x.get_source_path() for x in lst]
    src_name = [x.get_qualified_source_name() for x in lst]
    frame = pd.DataFrame(OrderedDict((('project', projects),
                                      ('commit', commit),
                                      ('path_test', path_test),
                                      ('test_name', test_name),
                                      ('path_src', path_src),
                                      ('class_name', src_name))))
    output = '{}/res_'.format(output)+project.get_project_name()+'.csv'
    frame.to_csv(output, index=False)


if __name__ == '__main__':
    project = '/tmp/lang_1_buggy'
    l = get_test_and_classes(project)
