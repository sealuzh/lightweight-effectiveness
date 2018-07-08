__author__ = "Giovanni Grano"
__email__ = "grano@ifi.uzh.ch"
__license__ = "MIT"

import warnings
from effectiveness.classification.classifier import *


def warn(*args, **kwargs):
    """Used to suppress sklearn warnings"""
    pass


warnings.warn = warn


def main():
    """
    This script run the machine learning classifier.
    Whether you invoke the classification method without specified algorithm argument,
    the nested cross-validation process will compare all the possible algorithms specified
    and will give in output the results for the best one found in such a process.
    Whether you want to run the classification and get the results for a single algorithm,
    specify it through the algorithm argument.
    For the sake of simplicity, you might just de-comment one of the lines of code below.
    """

    # De-comment to run only the KNN algorithm
    # classification(consider_coverage=True, n_inner=5, n_outer=10, algorithm='knn')
    # classification(consider_coverage=False, n_inner=5, n_outer=10, algorithm='knn')

    # De-comment to run only the SVC algorithm
    # classification(consider_coverage=True, n_inner=5, n_outer=10, algorithm='svc')
    # classification(consider_coverage=False, n_inner=5, n_outer=10, algorithm='svc')

    # De-comment to run only the RFC algorithm
    # classification(consider_coverage=True, n_inner=5, n_outer=10, algorithm='rfc')
    # classification(consider_coverage=False, n_inner=5, n_outer=10, algorithm='rfc')

    classification(consider_coverage=True, n_inner=5, n_outer=10)
    classification(consider_coverage=False, n_inner=5, n_outer=10)


if __name__ == '__main__':
    main()
