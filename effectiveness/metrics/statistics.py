import pandas as pd


def format2double(x):
    return '%1.2f' % x


def main():
    frame = pd.read_csv("rq1.csv")
    print(len(frame))
    frame = frame[frame.p_values <= 0.005]
    frame = frame[frame.cliff_delta != 'negligible']
    frame['rel'] = frame.cliff_estimate.apply(lambda x: '+' if x > 0 else '-')
    frame.cliff_estimate = frame.cliff_estimate.apply(lambda x: round(abs(x), ndigits=2))
    frame['d-value'] = frame.apply(lambda x: '{} ({})'.format(x.cliff_estimate, x.cliff_delta), axis=1)
    print(frame[['metrics', 'rel', 'd-value']].to_latex(index=False))


if __name__ == '__main__':
    main()
