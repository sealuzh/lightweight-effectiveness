import os

# the base dir of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RUBY = '/Users/grano/.rvm/rubies/ruby-2.2.1/bin'

SCRIPT_READABILITY = os.path.abspath(os.path.join(BASE_DIR, 'metrics/readability/compute_readability.rb'))

# the directory that contains the data
DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, 'data'))

# the installation directory of Defect4j in the system
DEFECT4J = '/Users/grano/Documents/PhD/defects4j/framework/bin'

METRICS_DIR = os.path.abspath(os.path.join(BASE_DIR, 'metrics'))

# test smell jar
TEST_SMELL_JAR = os.path.abspath(os.path.join(BASE_DIR, 'metrics/test-smells/test-smells.jar'))

# code smell jar
CODE_SMELL_JAR = os.path.abspath(os.path.join(BASE_DIR, 'metrics/code-quality/code-smells.jar'))

# ck metrics jar
CK_METRICS_JAR = os.path.abspath(os.path.join(BASE_DIR, 'metrics/code-quality/code-quality.jar'))

# readability path
READABILITY_PATH = os.path.abspath(os.path.join(BASE_DIR, 'metrics/readability'))

# the path that contains the projects
PROJECTS = os.path.abspath(os.path.join(BASE_DIR, 'projects'))

# the path that contains the mutation results
MUTATION_RESULTS = os.path.abspath(os.path.join(BASE_DIR, 'mutation_results'))

# the path of the Python package for the mutation
MUTATION_PACKAGE = os.path.abspath(os.path.join(BASE_DIR, 'effectiveness/mutation'))

RESULTS_DIR = os.path.abspath(os.path.join(BASE_DIR, 'results'))
