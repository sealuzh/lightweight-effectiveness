__author__ = "Giovanni Grano"
__license__ = "MIT"
__email__ = "grano@ifi.uzh.ch"

import pandas as pd
import glob
from effectiveness.settings import *


def process_results(mutation=METRICS_DIR+'/results.csv', smells=METRICS_DIR+'/test-smells.csv',
                    ck=METRICS_DIR+'/ck-metrics.csv',
                    code_smells=METRICS_DIR+'/code-smells',
                    readability=METRICS_DIR+'/readability',
                    output=METRICS_DIR+'/merge.csv'):
    """
    It aggregates into a single csv file all the metrics about mutation, coverage, smells and ck-metrics
    separately computed

    Aggregates the result from the mutation with the other metrics we compute
    :param mutation: the csv with mutation score and line coverage
    :param smells: the csv with the test smells
    :param ck: the csv with the code metrics
    :param code_smells: the directory that contains the code smells metrics (1 for each project)
    :param readability: the directory that contains the two files for the readability (1 for CUT, 1 for test)
    :param output: the output csv

    """
    if os.path.exists(mutation) and os.path.exists(smells) and os.path.exists(ck) and os.path.exists(code_smells)\
            and os.path.exists(readability):
        print("* Processing {}".format(mutation))
    else:
        print("* One or more input files are missing\nPlease check the previous steps of the pipeline")
        exit(0)

    mutation_frame = pd.read_csv(mutation)
    print("* Number of originally executed mutations = {}".format(len(mutation_frame)))
    mutation_frame = mutation_frame.dropna(subset=['mutation', 'line_coverage'])
    print("* Number of successfully mutation = {}".format(len(mutation_frame)))
    smells_frame = pd.read_csv(smells)
    ck_frame = pd.read_csv(ck)

    print("*-------------------------------------------")

    # filter according to the test smells we have
    all_tests = smells_frame['test-suite'].tolist()
    filtered_frame = mutation_frame[mutation_frame['test_name'].isin(all_tests)]
    print('* After smells \t{}'.format(len(filtered_frame)))

    print("*-------------------------------------------")

    # filter according to the ck metrics we have
    all_tests = ck_frame['className'].tolist()
    filtered_frame = filtered_frame[filtered_frame['test_name'].isin(all_tests)]
    filtered_frame = filtered_frame[filtered_frame['class_name'].isin(all_tests)]
    print('* After cks \t{}'.format(len(filtered_frame)))
    prod_readability = pd.read_csv('{}/source_readability.csv'.format(readability))
    all_classes = prod_readability['tested_class'].tolist()
    filtered_frame = filtered_frame[filtered_frame['class_name'].isin(all_classes)]
    print("* After class readability = {}".format(filtered_frame.shape[0]))
    test_readability = pd.read_csv('{}/test_readability.csv'.format(readability))
    all_tests = test_readability['tested_class'].tolist()
    filtered_frame = filtered_frame[filtered_frame['class_name'].isin(all_tests)]
    print("* After test readability = {}".format(filtered_frame.shape[0]))

    test_smells_metrics = ['isAssertionRoulette', 'isEagerTest', 'isLazyTest', 'isMysteryGuest',
                           'isSensitiveEquality', 'isResourceOptimism', 'isForTestersOnly',
                           'isIndirectTesting']
    code_ck_metrics = ['LOC', 'HALSTEAD', 'RFC', 'CBO', 'MPC', 'IFC', 'DAC', 'DAC2', 'LCOM1',
                       'LCOM2', 'LCOM3', 'LCOM4', 'CONNECTIVITY', 'LCOM5', 'COH', 'TCC', 'LCC', 'ICH',
                       'WMC', 'NOA', 'NOPA', 'NOP', 'McCABE', 'BUSWEIMER']
    code_smells_metrics = ['csm_CDSBP', 'csm_CC', 'csm_FD', 'csm_Blob', 'csm_SC', 'csm_MC', 'csm_LM', 'csm_FE']

    print("*-------------------------------------------")
    print("* Processing test smells:")
    for smell in test_smells_metrics:
        print("- Processing {}".format(smell))
        filtered_frame[smell] = filtered_frame.apply(lambda x: get_smell_value(x, smells_frame, smell), axis=1)

    print("*-------------------------------------------")
    print("* Processing ck metric for production:")
    for metric in code_ck_metrics:
        print("- Processing {}".format(metric))
        filtered_frame[metric+"_prod"] = filtered_frame.apply(lambda x: get_ck_value(x,
                                                                                     ck_frame,
                                                                                     metric),
                                                              axis=1)

    print("*-------------------------------------------")
    print("* Processing ck metric for tests:")
    for metric in code_ck_metrics:
        print("- Processing {}".format(metric))
        filtered_frame[metric+"_test"] = filtered_frame.apply(lambda x: get_ck_value(x,
                                                                                     ck_frame,
                                                                                     metric,
                                                                                     'test_name'),
                                                              axis=1)

    print("*-------------------------------------------")
    print("* Processing code smells for productions:")
    files = glob.glob(code_smells+'/*.csv')
    code_smell_frame = pd.concat([pd.read_csv(f) for f in files])
    for metric in code_smells_metrics:
        print("- Processing {}".format(metric))
        filtered_frame[metric] = filtered_frame.apply(lambda x: get_production_code_smell(x, code_smell_frame, metric),
                                                      axis=1)

    print("*-------------------------------------------")
    print("* Processing readability:")
    print("- Processing production readability")
    filtered_frame['prod_readability'] = filtered_frame.apply(lambda x: get_readability(x, prod_readability),
                                                              axis=1)
    print("- Processing test readability")
    filtered_frame['test_readability'] = filtered_frame.apply(lambda x: get_readability(x, test_readability),
                                                              axis=1)

    print("*-------------------------------------------")
    print("* Saving the aggregate in {}".format(output))
    filtered_frame.to_csv(output, index=False)


def get_process_metric(row, flag, ck_frame, metric, verbose=False):
    """
    Returns the value for the given metric for a particular source
    :param row: the data frame row for the test
    :param flag: true if that's a production class; false if a test
    :param ck_frame: the frame with all the ck metrics
    :param metric: the given metric

    """
    if flag:
        name = 'class_name'
    else:
        name = 'test_name'
    cut = row[name]

    aux = ck_frame[ck_frame['class'] == cut][metric]
    if len(aux) != 1 and verbose:
        print("\t* Two entries for {}".format(cut))
    return aux.iloc[0]


def get_readability(row, frame, key='class_name', verbose=False):
    """
    Returns the readability for the given production class or test
    :param row: the row of the original frame
    :param frame: the readability fame
    :param key: the key in the passed frame
    """
    cut = row[key]

    aux = frame[frame['tested_class'] == cut]['readability']
    if len(aux) != 1 and verbose:
        print("\t* {} entries for {}".format(str(len(aux)), cut))
    return aux.iloc[0]


def get_production_code_smell(row, frame, smell, key='class_name', verbose=False):
    """
    Returns the value for the given code smell for a production class
    :param row:
    :param frame:
    :param smell:
    :param key:
    """
    cut = row[key]
    aux = frame[frame['className'] == cut][smell]
    if len(aux) != 1 and verbose:
        print("\t* {} entries for {}".format(str(len(aux)), cut))
    return int(aux.iloc[0])


def get_smell_value(row, smells_frame, smell, key='test_name', verbose=False):
    """
    Returns the value for the given smell for a particular test
    :param row: the data frame row for the test
    :param smells_frame: the frame with all the smells
    :param smell: the kind of smell
    :param key: the key to look for in the frame
    """
    cut = row[key]
    aux = smells_frame[smells_frame['test-suite'] == cut][smell]
    if len(aux) != 1 and verbose:
        print("\t* {} entries for {}".format(str(len(aux)), cut))
    return aux.iloc[0]


def get_ck_value(row, ck_frame, metric, key='class_name', verbose=False):
    """
    Returns the value for the given metric for a particular source
    :param row: the data frame row for the test
    :param ck_frame: the frame with all the ck metrics
    :param metric: the given metric
    :param key: the key for the metric

    """
    cut = row[key]

    aux = ck_frame[ck_frame['className'] == cut][metric]
    if len(aux) != 1 and verbose:
        print("\t* {} entries for {}".format(str(len(aux)), cut))
    return aux.iloc[0]


def separate_sets(complete_frame=METRICS_DIR+'/merge.csv', delimiter='quartile',
                  name_good='good_tests', name_bad='bad_tests'):
    """
    It separates
    :param complete_frame: the frame to read with the metrics
    :param delimiter: the valued used to split the sets
    :param name_good: the name for the frame with the effective tests
    :param name_bad: the name for the frame with the non effective tests
    :return:
    """
    frame = pd.read_csv(complete_frame)
    median = frame.mutation.median()
    quantiles = frame.mutation.quantile([0.25, 0.75])
    lower_quantile = quantiles[0.25]
    upper_quantile = quantiles[0.75]

    if delimiter == 'quartile':
        bad_tests = frame[frame['mutation'] <= lower_quantile]
        good_tests = frame[frame['mutation'] >= upper_quantile]
        bad_tests.to_csv(os.path.join(DATA_DIR, '{}.csv'.format(name_good)), index=False)
        good_tests.to_csv(os.path.join(DATA_DIR, '{}.csv'.format(name_bad)), index=False)
        print("* Good tests quantile = {}".format(len(good_tests)))
        print("* Bad tests quantile = {}".format(len(bad_tests)))
    else:
        bad_tests = frame[frame['mutation'] <= median]
        good_tests = frame[frame['mutation'] > median]
        bad_tests.to_csv(os.path.join(DATA_DIR, '{}_median.csv'.format(name_good)), index=False)
        good_tests.to_csv(os.path.join(DATA_DIR, '{}_median.csv'.format(name_bad)), index=False)
        print("* Good tests median = {}".format(len(good_tests)))
        print("* Bad tests median = {}".format(len(bad_tests)))


def count_smells(complete_frame='merge.csv'):
    """
    Prints the number of the detected smells into the dataset
    :param complete_frame: the csv file to read
    """
    frame = pd.read_csv(complete_frame)
    test_smells_metrics = ['isAssertionRoulette', 'isEagerTest', 'isLazyTest', 'isMysteryGuest',
                           'isSensitiveEquality', 'isResourceOptimism', 'isForTestersOnly',
                           'isIndirectTesting']
    overall = 0
    for metric in test_smells_metrics:
        counts = frame[metric].sum()
        overall = overall + counts
        print('{} = {}'.format(metric, counts))
    print('Overall = {}'.format(overall))

    code_smells_metrics = ['csm_CDSBP', 'csm_CC', 'csm_FD', 'csm_Blob', 'csm_SC', 'csm_MC', 'csm_LM', 'csm_FE']

    overall = 0
    for metric in code_smells_metrics:
        counts = frame[metric].sum()
        overall = overall + counts
        print('{} = {}'.format(metric, counts))
    print('Overall = {}'.format(overall))


if __name__ == '__main__':

    for operator in ALL_OPERATORS:
        process_results(mutation=METRICS_DIR+'/results-{}.csv'.format(operator),
                    output=METRICS_DIR + '/merge-{}.csv'.format(operator))
        separate_sets(complete_frame=METRICS_DIR+'/merge-{}.csv'.format(operator),
                      name_good='good_tests-{}'.format(operator),
                      name_bad='bad_tests-{}'.format(operator))
    # process_results()
    # separate_sets()
