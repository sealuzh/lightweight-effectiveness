import os 
import fnmatch
import re
import glob

__author__ = "Giovanni Grano"
__license__ = "MIT"
__email__ = "grano@ifi.uzh.ch"


class Project:
    """
    This classes is used to mine a cloned repository and extract matches between tests and classes
    under test
    """

    def __init__(self, project, include_pattern, exclude_pattern, path):
        self.__project = project
        self.__path = path
        self.__include_pattern = include_pattern
        self.__include_pattern = [x.replace('.class', '.java') if '.class' in x else x
                                  for x in self.__include_pattern]
        self.__exclude_pattern = exclude_pattern
        self.__list_matches = []

    def get_project_name(self):
        """Returns the name of the project"""
        return self.__project

    def get_project_path(self):
        """Returns the absolute path of the project"""
        return self.__path

    def get_tests(self, test_dir, src_dir):
        """Returns a list of Pair object, i.e., a list of matched tests and classes under test
        based on the pattern extracted from the pom
    
        Arguments
        -------------
        - src_dir: the directory that contains the source code of the project

        """
        # pattern = self.__include_pattern[0][3:]
        pattern = self.__include_pattern[0]
        exclude_pattern = '1234567'
        if len(self.__exclude_pattern) > 0:
            exclude_pattern = self.__exclude_pattern[0][3:]
        self.recursive_glob(test_dir, pattern, exclude_pattern)
        self.look_for_cuts(src_dir)
        self.__list_matches = [i for i in self.__list_matches if i.get_qualified_source_name()]
        print("\t- Tests for {} = {}".format(self.__project, len(self.__list_matches)))
        return self.__list_matches

    def look_for_cuts(self, src_dir='.'):
        """Search for the class under test that matches with te tests
    
        Arguments
        -------------
        - src_dir: the directory that contains the source code of the project

        """
        for i, pair in enumerate(self.__list_matches):
            # get path of test
            test_path = pair.get_test_path()
            # get name to look for
            pattern = self.__include_pattern[0][3:] # todo: check here this
            to_look_for = self.get_name_class_according_to_pattern(test_path, pattern)
            src_path, qualified_name = self.recursive_glob_src(src_dir, to_look_for)
            if src_path is None and qualified_name is None:
                continue
            else:
                self.__list_matches[i].set_source(src_path, qualified_name)

    @staticmethod
    def get_name_class_according_to_pattern(test_path, pattern):
        """Returns the name of the test file from production code, according to the found test case and
        ot the include patter

        Arguments
        -------------
        - test_path: the path for the found test
        - pattern: the include patter for the test

        """
        if pattern.startswith('Test*'):
            m = re.search(r"^[^.*]*", pattern, re.M)
            to_remove = m.group(0)
            return os.path.basename(test_path).replace(to_remove, '')
        # customization done for checkstyle
        # in this case, the include is com/puppycrawl/**/*.java
        # when the true pattern is *Test.java
        elif pattern.endswith('/*.java'):
            return os.path.basename(test_path).replace('Test.java', '.java')
        # customization done for commons-io
        elif '*Test*' in pattern:
            if 'TestCase' in pattern:
                return os.path.basename(test_path).replace('TestCase', '')
            else:
                return os.path.basename(test_path).replace('Test', '')
        else:
            return os.path.basename(test_path).replace(pattern[1:], '.java')

    def recursive_glob(self, root_dir='.', pattern='*Test.java', exclude='1234567'):
        """Search recursively for files matching a specified pattern and look for its qualified name.
        This method should be used to identify tests

        Arguments
        -------------
        - root_dir: the directory of the project
        - pattern: the pattern for the tests specified into the pom file
        - exclude: exclude pattern for tests extracted from the pom file

        """
        look_for = root_dir + pattern
        file_names = glob.glob(look_for, recursive=True)
        for filename in file_names:
            if not fnmatch.fnmatch(filename, exclude):
                qualified_name = self.get_full_qualified_name(filename)
                self.__list_matches.append(Pair(self.__project, filename, qualified_name))
        return None, None

    def recursive_glob_src(self, rootdir='.', pattern='*Test.java'):
        """Search recursively for files matching a specified pattern and look for its qualified name.
        This method should be used to identify the source files, given the name of the test and the pattern

        Arguments
        -------------
        - rootdir: the directory of the source for the project
        - pattern: the pattern for the source to look for

        """
        look_for = rootdir + "**/" + pattern
        filenames = glob.glob(look_for, recursive=True)
        if bool(filenames):
            qualified_name = self.get_full_qualified_name(filenames[0])
            return filenames[0], qualified_name
        return None, None

    def get_full_qualified_name(self, path):
        """Returns the fully qualified name for a class
        
        Arguments
        -------------
        - path: the path of the class

        """
        with open(path, encoding="utf8", errors='ignore') as f:
            for line in f:
                if line.startswith('package'):
                    name = line.replace('package', '').strip()
                    aux = os.path.basename(path).replace('.java', '')
                    return name[:-1] + '.' + aux


class Pair:
    """
    This class represents a match between a test case and a file name based on the textual pattern
    extracted from the pom file
    """

    def __init__(self, project, test_case_path, test_name):
        self.__project = project
        self.__test_case_path = test_case_path
        self.__test_name = test_name
        self.__source_path = ''
        self.__source_name = ''

    def set_source(self, source_path, source_name):
        """Sets the name of the class and its path

        Arguments
        -------------
        - source_path: the path of the matched class
        - source_name: the full qualified name of the matched class
        """

        self.__source_path = source_path
        self.__source_name = source_name

    def get_project(self):
        """Returns the name of the project"""
        return self.__project

    def get_test_path(self):
        """Returns the path for the found test case"""
        return self.__test_case_path

    def get_qualified_source_name(self):
        """Returns the qualified name for the matched class"""
        return self.__source_name

    def get_qualified_test_name(self):
        """Returns the qualified name for the found test case"""
        return self.__test_name

    def get_source_path(self):
        """Returns the path for the matched class"""
        return self.__source_path

    def __str__(self):
        """Returns a stringified representation of the class"""
        return "*\nProject\t = {}\nTest\t = {}\nClass\t = {}".format(self.__project, self.__test_name, self.__source_name)

