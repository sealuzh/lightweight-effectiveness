from __future__ import division
from html.parser import HTMLParser

__author__ = "Giovanni Grano"
__license__ = "MIT"
__email__ = "grano@ifi.uzh.ch"


class PitestHTMLParser(HTMLParser):
    """This class is used to parse the html results of pitest mutation"""

    def __init__(self, test_file):
        """

        :param test_file:
        """
        HTMLParser.__init__(self)
        self.__flag_line = False
        self.__flag_mutation = False
        self.__coverage_tag_found = 0
        self.__test_file = test_file
        f = open(self.__test_file)
        self.__content = f.read()
        self.__line_coverage = 0
        self.__mutation_coverage = 0.0
        self.__no_mutations = 0
        self.feed(self.__content)

    def handle_starttag(self, tag, attrs):
        """ Process the start tag

        :param tag: the current tag
        :param attrs: the attributes for the current tag
        """
        if tag == 'div':
            if attrs:
                tuple_dict = dict(attrs)
                if tuple_dict.get('class') == 'coverage_legend':
                    self.__coverage_tag_found += 1

    def handle_data(self, data):
        """
        The content of a tag

        :param data: the content
        """
        if self.__coverage_tag_found == 1 and not self.__flag_line:
            covered_lines = float(data.split('/')[0])
            lines = float(data.split('/')[1])
            if lines == 0:
                self.__line_coverage == float('nan')
            else:
                self.__line_coverage = covered_lines/lines
            self.__flag_line = True

        if self.__coverage_tag_found == 2 and not self.__flag_mutation:
            killed_mutants = float(data.split('/')[0])
            total_mutants = float(data.split('/')[1])
            if total_mutants == 0:
                self.__mutation_coverage == float('nan')
            else:
                self.__mutation_coverage = killed_mutants/total_mutants
                self.__no_mutations = total_mutants

            self.__flag_mutation = True

    def handle_endtag(self, tag):
        pass

    def get_mutation_coverage(self):
        """
        :return: the computed mutation coverage
        """
        return self.__mutation_coverage

    def get_line_coverage(self):
        """
        :return: the computed line coverage
        """
        return self.__line_coverage

    def get_no_mutants(self):
        """
        :return: the number of mutants
        """
        return self.__no_mutations

    def error(self, message):
        pass


if __name__ == '__main__':
    test = PitestHTMLParser("/Users/grano/Documents/PhD/mutation_tc_quality/scripts_mutation/"
                            "mutation_results/checkstyle/com.puppycrawl.tools.checkstyle.ant."
                            "CheckstyleAntTaskTest/201803080824/index.html")
