import pandas as pd
from effectiveness.settings import *

def format2double(x):
    return '%1.2f' % x


def main():
    frame = pd.read_csv("rq1.csv")
    print(len(frame))
    frame = frame[frame.p_values <= 0.05]
    frame = frame[frame.cliff_delta != 'negligible']
    frame['rel'] = frame.cliff_estimate.apply(lambda x: '+' if x > 0 else '-')
    frame.cliff_estimate = frame.cliff_estimate.apply(lambda x: round(abs(x), ndigits=2))
    frame['d-value'] = frame.apply(lambda x: '{} ({})'.format(x.cliff_estimate, x.cliff_delta), axis=1)
    print(frame.shape[0])
    print(frame[['metrics', 'rel', 'd-value']].to_latex(index=False))


def generate_frames_for_replication_package(filter_for_negligible=True, destination=RQ1_DIR):
    for operator in ALL_OPERATORS:
        frame = pd.read_csv('{}/rq1-{}.csv'.format(RQ1_DIR, operator))
        frame = frame[frame.p_values <= 0.05]
        if filter_for_negligible:
            frame = frame[frame.cliff_delta != 'negligible']
        if not frame.empty:
            frame['rel'] = frame.cliff_estimate.apply(lambda x: '+' if x > 0 else '-')
            frame.cliff_estimate = frame.cliff_estimate.apply(lambda x: round(abs(x), ndigits=2))
            frame['d-value'] = frame.apply(lambda x: '{} ({})'.format(x.cliff_estimate, x.cliff_delta), axis=1)
            frame = frame[['metrics', 'rel', 'd-value']]
            frame.to_csv('{}/factors-{}.csv'.format(destination, operator), index=False)


if __name__ == '__main__':
    generate_frames_for_replication_package(destination='/Users/grano/Documents/PhD/research-projects/lightweight-effectiveness/lightweight-effectiveness-replication/factors-single-mutators')
    # main()
