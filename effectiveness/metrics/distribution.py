import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

def main(plot):
    """
    :plot 0 for everything, 1 for only quantiles, 2 for only median
    """
    frame = pd.read_csv('merge.csv')
    median = frame.mutation.median()
    quantiles = frame.mutation.quantile([0.25, 0.75])
    lower_quantile = quantiles[0.25]
    upper_quantile = quantiles[0.75]

    q1 = frame[frame['mutation'] <= lower_quantile]['mutation'].tolist()
    q4 = frame[frame['mutation'] >= upper_quantile]['mutation'].tolist()
   
    low_med = frame[frame['mutation'] <= median]['mutation'].tolist()
    above_med = frame[frame['mutation'] > median]['mutation'].tolist()
    
    low = go.Box(
        name='1Q',
        y=q1
    )
    high = go.Box(
        name='4Q',
        y=q4
    )
    entire = go.Box(
        name='All',
        y=frame['mutation'].tolist()
        )
    low_med = go.Box(
        name='< median',
        y=low_med
    )
    above_med = go.Box(
        name='> median',
        y=above_med
    )
    layout = go.Layout(
    xaxis=dict(
        tickfont=dict(
            size=16,
            color='black'
            ),
        ),
    yaxis=dict(
        title=' %mutation score',
        tickfont=dict(
            size=16,
            color='black'
            ),
        ),
    autosize=True,
    legend=dict(
    font=dict(
        size=16,
        color='black'
        ),
    )
    )

    if (plot == 0):
        data = [entire, low, high, low_med, above_med]
        name = 'plots/all_distribution.pdf'
    elif (plot == 1): 
        data = [entire, low, high]
        name = 'plots/study_one_distribution.pdf'
    else:
        data = [entire, low_med, above_med]
        name = 'plots/study_two_distribution.pdf'
    fig = go.Figure(data=data, layout=layout)
    py.image.save_as(fig, name)

if __name__ == '__main__':
    main(1)
