import pandas as pd
from effectiveness.settings import *


def context_study_stats(frame_path=METRICS_DIR+'/merge.csv'):
    """
    Returns the latex code for the context of the study table
    :param frame_path: the path with all the raw data
    :return: prints the latex code
    """
    frame = pd.read_csv(frame_path)
    print(frame['LOC_prod'].mean())
    print(frame['LOC_prod'].sum())
    print(frame['LOC_test'].sum())
    print(frame['no_mutations'].sum())
    print(frame.shape[0])

    sizes = frame.groupby('project').size()
    prod = frame.groupby('project')['LOC_prod'].sum( )
    test = frame.groupby('project')['LOC_test'].sum()
    mutants = frame.groupby('project')['no_mutations'].sum()

    result = pd.DataFrame({'project': list(sizes.index),
                           'size': list(sizes),
                           'prod': list(prod),
                           'test': list(test),
                           'mutants': list(mutants)},
                          columns=['project', 'size', 'prod', 'test', 'mutants'])
    print(result.to_latex())


if __name__ == '__main__':
    context_study_stats()
