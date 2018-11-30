from effectiveness.mutation.mutation_calc import *
from effectiveness.mutation.pitest_html_parser import *
from effectiveness.settings import *
import glob
import os

__author__ = "Giovanni Grano"
__license__ = "MIT"
__email__ = "grano@ifi.uzh.ch"


def calculate_results(default_dir=RESULTS_DIR, clean=True, name='results'):
    """Aggregates all the mutations calculated and add the information about the mutation

    Arguments
    -------------
    :param default_dir: the dir where all the csv files are stores
    :param clean: flag to remove classes with no mutations
    :param name: the name of the output file
    """
    if not os.path.isdir(default_dir):
        print("No dir to process! You're missing some previous steps")
        exit(0)
    result_csv = glob.glob(default_dir+'/res_*.csv')
    frames = []
    for project in result_csv:
        frames.append(pd.read_csv(project))
    aggregate = pd.concat(frames)
    aggregate[['module']] = aggregate[['module']].fillna(value='')
    aggregate['mutation'] = aggregate.\
        apply(lambda x: get_mutation_value_html(row=x,
                                                path_mutation=MUTATION_RESULTS+'-'+operator),
              axis=1)
    aggregate['no_mutations'] = aggregate.\
        apply(lambda x: get_mutation_value_html(row=x,
                                                ret_no_mutation=True,
                                                path_mutation=MUTATION_RESULTS + '-' + operator),
              axis=1)
    aggregate['line_coverage'] = aggregate.\
        apply(lambda x: get_mutation_value_html(row=x,
                                                ret_no_mutation=False,
                                                ret_line_cov=True,
                                                path_mutation=MUTATION_RESULTS+'-'+operator), axis=1)

    if clean:
        print('Rows before the cleaning = {}'.format(aggregate.shape[0]))
        aggregate = aggregate.dropna()
        aggregate = aggregate[aggregate['no_mutations'] != 0]
        print('Rows after the cleaning = {}'.format(aggregate.shape[0]))
    aggregate.to_csv('{}/{}.csv'.format(METRICS_DIR, name), index=False)


def get_mutation_value_html(row, ret_no_mutation=False, ret_line_cov=False, path_mutation=MUTATION_RESULTS):
    """Functions called into the lambda to calculate the mutation
    The output from pitest needs to be in HTML format

    Arguments
    -------------
    :param row: the row of the of the data frame
    :param ret_no_mutation: if true, returns the number of mutations; if false, the mutation score
    :param ret_line_cov: line the parameter above
    :param path_mutation: the path where the mutation is
    """
    module_name = row.module
    if module_name == '':
        path = '{}/'.format(path_mutation) + row.project + '/' + row.test_name + '/**/index.html'
    else:
        path = '{}/'.format(path_mutation) + row.project + '/' + module_name + '-' + row.test_name + '/**/index.html'
    mutation_file = glob.glob(path, recursive=True)
    if not mutation_file:
        # no file = no mutations
        return None
    html_parser = PitestHTMLParser(mutation_file[0])
    if ret_line_cov:
        return html_parser.get_line_coverage()
    if ret_no_mutation:
        return html_parser.get_no_mutants()
    return html_parser.get_mutation_coverage()


def get_mutation_value(row, ret_no_mutation=False):
    """Functions called into the lambda to calculate the mutation
    The output from pitest needs to be in CSV format

    Arguments
    -------------
    - row: the row of the of the data frame
    - ret_no_mutation: if true, returns the number of mutations; if false, the mutation score

    """
    module_name = row.module
    if module_name == '':
        path = '{}/'.format(MUTATION_RESULTS) + row.project + '/' + row.test_name + '/**/index.html'
    else:
        path = '{}/'.format(MUTATION_RESULTS) + row.project + '/' + module_name + '-' + row.test_name + '/**/index.html'
    mutation_file = glob.glob(path, recursive=True)
    # used to reuse the expensive glob search
    if not mutation_file:
        return None
    if ret_no_mutation:
        return get_number_of_mutations(mutation_file[0])
    mutation = calc_coverage(mutation_file[0])
    return mutation


def get_number_of_mutations(path):
    """Returns the number of mutations for the class in the given path

    Arguments
    -------------
    - path: the path of the csv file for the current mutation

    """
    if not path:
        return 0
    return get_number_mutation(path)


if __name__ == '__main__':
    for operator in ALL_OPERATORS:
        calculate_results(name='results-{}'.format(operator))
    # calculate_results()
