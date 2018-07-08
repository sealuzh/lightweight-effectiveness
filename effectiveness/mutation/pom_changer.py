import sys
import os

__author__ = "Giovanni Grano"
__license__ = "MIT"
__email__ = "grano@ifi.uzh.ch"


def get_pitest_maven_skeleton(class_to_mutate, test_to_run, threads=4):
    """Returns the string to inject into the pom to run the mutation analysis

    Arguments
    -------------
    - class_to_mutate: the name of the class
    - test_to_run: the name of the test to run against the mutation
    - threads: the number of tests to use

    """
    string_to_inject = """
    <plugin>
    <groupId>org.pitest</groupId>
    <artifactId>pitest-maven</artifactId>
    <version>1.3.2</version>
    <configuration>
    <targetClasses>
    <param>
    """+class_to_mutate+"""
    </param>
    </targetClasses>
    <targetTests>
    <param>
    """+test_to_run+"""
    </param>
    </targetTests>
    <avoidCallsTo>
    <threads>"""+str(threads)+"""</threads>
    <avoidCallsTo>java.util.logging</avoidCallsTo>
    <avoidCallsTo>org.apache.log4j</avoidCallsTo>
    <avoidCallsTo>org.slf4j</avoidCallsTo>
    <avoidCallsTo>org.apache.commons.logging</avoidCallsTo>
    </avoidCallsTo>
    </configuration>
    </plugin>
    """
    return string_to_inject


def generate_new_pom(project, class_to_mutate, test_to_run):
    """Generates a new pom, reading the cached one in cached_pom.xml, adding the
    pitest maven goal

    Arguments
    -------------
    - project: the path for the project
    - class_to_mutate: the fully qualified name for the class to mutate
    - test_to_run: the name for the test to run against the mutation

    """
    try:
        os.remove('pom.xml')
    except OSError as e:
        pass 

    build_flag = False
    written_flag = False
    aux_pom = open('cached_pom.xml', 'r')

    with open('pom.xml', 'w') as new_pom:
        for line in aux_pom.readlines():
            if build_flag and line.strip().startswith('<plugins>'):
                write_line(new_pom, line)
                write_pitest_pom(new_pom, class_to_mutate, test_to_run)
                build_flag = False
                written_flag = True
                continue
            if line.strip().startswith('<build>') and not written_flag:
                build_flag = True
            write_line(new_pom, line)


def write_line(write, line):
    """Writes a line from the cached pom to the new one

    Arguments
    -------------
    - write: output file
    - line: line to write to the file

    """
    write.write(line)


def write_pitest_pom(write, class_to_mutate, test_to_run):
    """Writes the injected pitest goal into the new pom

    Arguments
    -------------
    - write: output file
    - class_to_mutate: the fully qualified name for the class to mutate
    - test_to_run: the name for the test to run against the mutation

    """
    write.write(get_pitest_maven_skeleton(class_to_mutate, test_to_run))


if __name__ == '__main__':
    project_name = sys.argv[1]
    class_to_mutate = sys.argv[2]
    test_to_run = sys.argv[3]
    generate_new_pom(project_name, class_to_mutate, test_to_run)
