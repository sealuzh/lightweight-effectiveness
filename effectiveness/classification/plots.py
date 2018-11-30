import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
from effectiveness.settings import *
py.sign_in('*******', '*******')


def main(frame, models=['dynamic', 'static'], technique='rfc'):
    f = pd.read_csv(frame, index_col=0)
    features_importance = []
    for index, row in f.iterrows():
        features_importance.append(row.mean())
    metrics = f.index.values

    s = sorted(zip(map(lambda x: round(x, 3), features_importance), metrics), reverse=True)
    print(s[0:20])
    if model == 'static':
        plot_feature_importance(s[0:20], '{}-{}'.format(model, technique))
    else:
        plot_fancy_thing(s[0:20], '{}-{}'.format(model, technique))


def plot_fancy_thing(metrics, output_name):
    """
    Draws a bar plot of the metrics passed as parameter;
    It requires a plotly account to be locally installed on the machine
    :param metrics: the metrics to plot
    :param name: the name of the metrics
    """
    values, names = zip(*metrics)

    names = [x.replace('CONNECTIVITY', 'CONNECT.') for x in names]
    names = [x.replace('_prod', ' prod.') for x in names]
    names = [x.replace('_test', ' test') for x in names]
    names = [x.replace('csm_', '') for x in names]
    names = [x.replace('_', ' ') for x in names]
    names = [x.replace('is', '') for x in names]

    data = []
    index = 0
    for value, name in zip(values, names):
        aux_values = []
        is_cov = True if name == 'line coverage' else False
        if is_cov:
            aux_values.append(value)
            aux_values.append(0)
        else:
            aux_values.append(0)
            aux_values.append(value)
        data.append(
            go.Bar(
                x=aux_values,
                y=['line cov.', 'others'],
                orientation='h',
                name=name
            )
        )
        index = index+1

    layout = go.Layout(
        xaxis=dict(
            title="Mean Decrease in Impurity",
            titlefont=dict(
              size=16,
              color='black'
            ),
            tickfont=dict(
                size=16,
                color='black'
            ),
        ),
        yaxis=dict(
            titlefont=dict(
                size=16,
                color='black'
            ),
            tickfont=dict(
                size=16,
                color='black'
            ),
        ),
        autosize=True,
        margin=go.Margin(
            l=80,
            r=50,
            b=70,
            t=20,
            pad=10
        ),
        legend=dict(
            font=dict(
                size=13,
                color='black'
            )
            # ,
            # x=-.1
        ),
        barmode='stack'
    )

    fig = go.Figure(data=data, layout=layout)
    py.image.save_as(fig, filename='{}/{}.pdf'.format(PLOT_DIR, output_name))


def plot_feature_importance(metrics, output_name):
    """
    Draws a bar plot of the metrics passed as parameter;
    It requires a plotly account to be locally installed on the machine
    :param metrics: the metrics to plot
    :param output_name: the name of the metrics
    """
    values, names = zip(*metrics)
    names = [x.replace('CONNECTIVITY', 'CONNECT.') for x in names]
    names = [x.replace('_prod', ' prod.') for x in names]
    names = [x.replace('_test', ' test') for x in names]
    names = [x.replace('csm_', '') for x in names]
    names = [x.replace('_', ' ') for x in names]
    names = [x.replace('is', ' ') for x in names]

    data = [go.Bar(
        x=values,
        y=names,
        orientation='h',
    )]

    layout = go.Layout(
        xaxis=dict(
            title="Mean Decrease in Impurity",
            titlefont=dict(
              size=16,
              color='black'
            ),
            tickfont=dict(
                size=16,
                color='black'
            ),
        ),
        yaxis=dict(
            titlefont=dict(
                size=16,
                color='black'
            ),
            tickfont=dict(
                size=16,
                color='black'
            ),
        ),
        autosize=True,
        margin=go.Margin(
            l=160,
            r=50,
            b=70,
            t=20,
            pad=10
        ),
        legend=dict(
            font=dict(
                size=6
            ),
        )
    )

    fig = go.Figure(data=data, layout=layout)
    py.image.save_as(fig, filename='{}/{}.pdf'.format(PLOT_DIR, output_name))


if __name__ == '__main__':
    models = ['dynamic', 'static']
    technique = 'rfc'
    for model in models:
        path = os.path.join(DATA_DIR, 'features_importance_{}_{}.csv'.format(model, technique))
        if os.path.exists(path):
            main(path)
