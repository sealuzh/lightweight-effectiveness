from __future__ import division
import pandas as pd
import sys

__author__ = "Giovanni Grano"
__license__ = "MIT"
__email__ = "grano@ifi.uzh.ch"


def calc_coverage(csv_file):
    """Return the mutation coverage from the csv output of pitest
    Arguments
    -------------
    - csv_file: the path of the csv file storing the result of the mutation
    """
    frame = pd.read_csv(csv_file, names=['class', 'name', 'mutation', 'operation', 'line', 'killed', 'test'])
    mutations = len(frame)
    if mutations == 0:
        return None
    are_killed = frame.killed.str.contains('KILLED').sum(0) > 1
    if are_killed:
        killed = frame.killed.value_counts()['KILLED']
    else:
        return 0
    return killed/mutations


def get_number_mutation(csv_file):
    """Return the number of mutations done for a class
    Arguments
    -------------
    - csv_file: the path of the csv file storing the result of the mutation
    """
    frame = pd.read_csv(csv_file, names=['class', 'name', 'mutation', 'operation', 'line', 'killed', 'test'])
    return len(frame)


if __name__ == '__main__':
    path = sys.argv[1]
    coverage = calc_coverage(path)
    print('Mutation coverage computed = {}'.format(coverage))