__author__ = "Giovanni Grano"
__email__ = "grano@ifi.uzh.ch"
__license__ = "MIT"

import numpy as np
import matplotlib

matplotlib.use('Agg')
from matplotlib import pyplot as plt
from sklearn.externals import joblib

from sklearn.model_selection import train_test_split, RepeatedStratifiedKFold, GridSearchCV, StratifiedKFold, \
    cross_validate
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, \
    mean_absolute_error, make_scorer, brier_score_loss, roc_curve

from sklearn.preprocessing import OneHotEncoder
from effectiveness.classification.plots import *

from sklearn.utils import shuffle
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


def import_frame(consider_coverage=True):
    """
    Imports all the data needed
    :param consider_coverage: boolean value to take into account or not the coverage
    :return: a tuple with the frame and the metrics
    """

    positive_example = pd.read_csv('{}/good_tests.csv'.format(DATA_DIR))
    negative_example = pd.read_csv('{}/bad_tests.csv'.format(DATA_DIR))
    index = 8 if consider_coverage else 9
    metrics = positive_example.columns[index:-10].tolist()
    positive_example['y'] = positive_example.apply(lambda x: 1, axis=1)
    negative_example['y'] = negative_example.apply(lambda x: 0, axis=1)

    frame = shuffle(pd.concat([positive_example, negative_example]))

    return frame, metrics


def plot_learning_curve(train_sizes, train_scores, test_scores):
    """Plots the learning curve"""
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)

    plt.figure()
    plt.xlabel("Training examples")
    plt.ylabel("Score")
    plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1,
                     color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.1, color="g")
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
             label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
             label="Cross-validation score")
    plt.legend(loc="best")
    plt.savefig('{}/learning_curve_{}.pdf'.format(DATA_DIR, coverage_suffix), bbox_inches='tight')


def get_param_grid(algorithm, metrics):
    """
    Returns the right parameter grid according to the selected algorithm
    :param algorithm: the algorithm to choose
    :param metrics: the list of metrics
    :return: a dictionary with the parameter grid
    """
    if algorithm == 'all':
        return [{'classifier': [SVC(probability=True)],
                 'preprocessing': [StandardScaler(), None],
                 'classifier__gamma': [0.01, 0.1, 1, 10, 100],
                 'classifier__C': [0.01, 0.1, 1, 10, 100]},
                {'classifier': [RandomForestClassifier()],
                 'preprocessing': [None],
                 'classifier__n_estimators': [3 * x for x in range(1, 11)],
                 'classifier__max_features': [int((len(metrics) / 10) * x) for x in range(1, 11)],
                 'classifier__max_depth': [5 * x for x in range(1, 11)],
                 'classifier__min_samples_leaf': [2 * x for x in range(1, 11)]},
                {'classifier': [KNeighborsClassifier()],
                 'preprocessing': [None],
                 'classifier__n_neighbors': [x for x in range(1, 15)],
                 'classifier__weights': ['uniform', 'distance'],
                 'classifier__leaf_size': [5 * x for x in range(1, 11)]}]
    elif algorithm == 'rfc':
        return [{'classifier': [RandomForestClassifier()],
                 'preprocessing': [None],
                 'classifier__n_estimators': [3 * x for x in range(1, 11)],
                 'classifier__max_features': [int((len(metrics) / 10) * x) for x in range(1, 11)],
                 'classifier__max_depth': [5 * x for x in range(1, 11)],
                 'classifier__min_samples_leaf': [2 * x for x in range(1, 11)]}]
    elif algorithm == 'svc':
        return [{'classifier': [SVC(probability=True)],
                 'preprocessing': [StandardScaler(), None],
                 'classifier__gamma': [0.01, 0.1, 1, 10, 100],
                 'classifier__C': [0.01, 0.1, 1, 10, 100]}]
    elif algorithm == 'knn':
        return [{'classifier': [KNeighborsClassifier()],
                 'preprocessing': [None],
                 'classifier__n_neighbors': [x for x in range(1, 15)],
                 'classifier__weights': ['uniform', 'distance'],
                 'classifier__leaf_size': [5 * x for x in range(1, 11)]}]
    elif algorithm == 'test':
        return [{'classifier': [KNeighborsClassifier()],
                 'preprocessing': [None],
                 'classifier__n_neighbors': [5]},
                {'classifier': [RandomForestClassifier()],
                 'preprocessing': [None],
                 'classifier__n_estimators': [3]}]
    else:
        print('Unsupported algorithm selected')
        exit()


def classification(consider_coverage=True, n_inner=5, n_outer=10, algorithm='all'):
    """
    Runs the entire process of classification and evaluation
    :param consider_coverage: to include or not the line coverage as a feature
    :param n_inner: number of folds for the inner cross fold validation
    :param n_outer: number of folds for the outer cross fold validation
    :param algorithm: select the algorithm to run; possible choices are 'svc', 'rfc', 'knn' and 'all'
    Validate and save a ML model
    """
    global X, Y, coverage_suffix

    # the suffix for saving the files
    coverage_suffix = 'dynamic' if consider_coverage else 'static'

    # Import the data
    print('Importing data')
    frame, metrics = import_frame(consider_coverage)
    print('Import: DONE')

    X = frame[metrics]
    Y = frame['y']

    pipe = Pipeline([('preprocessing', StandardScaler()),
                     ('classifier', SVC())])

    # Set up the algorithms to tune, train and evaluate
    param_grid = get_param_grid(algorithm, metrics)

    inner_cv = StratifiedKFold(n_splits=n_inner, shuffle=True)
    outer_cv = RepeatedStratifiedKFold(n_splits=n_outer, n_repeats=10)

    # inner cross validation
    grid = GridSearchCV(estimator=pipe,
                        param_grid=param_grid,
                        cv=inner_cv,
                        scoring=get_scoring(),
                        refit='roc_auc_scorer',
                        return_train_score=True,
                        verbose=1,
                        n_jobs=-1)

    results = cross_validate(estimator=grid,
                             cv=outer_cv,
                             X=X,
                             y=Y,
                             scoring=get_scoring(),
                             return_train_score=True,
                             verbose=1,
                             n_jobs=-1)

    accuracy = results.get('test_accuracy').mean()
    precision = results.get('test_precision').mean()
    recall = results.get('test_recall').mean()
    f1_score = results.get('test_f1_score').mean()
    roc_auc = results.get('test_roc_auc_scorer').mean()
    mae = results.get('test_mean_absolute_error').mean()
    brier = results.get('test_brier_score').mean()

    print('Performances:\n'
          'Accuracy\t {:.3f}\n'
          'Precision\t {:.3f}\n'
          'Recall\t {:.3f}\n'
          'F1 Score\t {:.3f}\n'
          'ROC AUC\t {:.3f}\n'
          'MAE\t {:.3f}\n'
          'Brier Score\t {:.3f}\n'.format(accuracy, precision, recall, f1_score, roc_auc, mae, brier))

    # save performance metrics
    metrics_res = pd.DataFrame({'accuracy': [accuracy],
                                'precision': [precision],
                                'recall': [recall],
                                'f1_score': [f1_score],
                                'ROC-AUC': [roc_auc],
                                'MAE': [mae],
                                'Brier': [brier]})

    metrics_res.to_csv('{}/evaluation_{}_{}.csv'.format(DATA_DIR, coverage_suffix, algorithm), index=False)

    grid.fit(X, Y)
    model = grid.best_params_['classifier']
    print('Best model is:\n{}'.format(model))
    model_string = open('{}/_model_{}_{}.txt'.format(DATA_DIR, coverage_suffix, algorithm), 'w')
    model_string.write(str(model))
    model_string.close()

    if type(model) is RandomForestClassifier:
        compute_mean_decrease_in_entropy(grid=model,
                                         n_outer=n_outer,
                                         metrics=metrics,
                                         algorithm=algorithm)

    print('Saving the model on the entire set')
    grid.fit(X, Y)
    joblib.dump(grid.best_estimator_, '{}/model_{}_{}.pkl'.format(DATA_DIR, coverage_suffix, algorithm), compress=1)


def compute_features_importance(grid, n_outer, metrics, algorithm):
    """
    Computes and saves the features importance with the Mean Decrease Accuracy approach
    :param grid: the model
    :param n_outer: the number of times to fit the model
    :param metrics: the list of metrics
    :param algorithm: the employed algorithm
    """
    features = [[] for _ in range(len(metrics))]

    for i in range(0, n_outer):
        grid.fit(X, Y)
        model = grid.best_params_['classifier']
        for j, elem in enumerate(model.feature_importances_):
            features[j].append(elem)
    runs = list(range(n_outer))
    features_importance = pd.DataFrame(features, columns=runs, index=metrics)
    features_importance.to_csv('{}/features_importance_{}_{}.csv'.format(DATA_DIR, coverage_suffix, algorithm))
    mean = lambda x: sum(x) / len(x)
    features_average = [mean(x) for x in features]
    s = sorted(zip(map(lambda x: round(x, 3), features_average), metrics), reverse=True)


def compute_mean_decrease_in_entropy(grid, n_outer, metrics, algorithm):
    """
    Computes and saves the feature importance computed with the Mean Decrease in Entropy approach
    :param grid: the model
    :param n_outer: the number of times to fit the model
    :param metrics: the list of metrics
    :param algorithm: the employed algorithm
    """
    features = [[] for _ in range(len(metrics))]
    for i in range(0, n_outer):
        grid.fit(X, Y)
        for j, elem in enumerate(grid.feature_importances_):
            features[j].append(elem)

    runs = list(range(n_outer))
    features_importance = pd.DataFrame(features, columns=runs, index=metrics)
    features_importance.to_csv('{}/features_importance_{}_{}.csv'.format(DATA_DIR, coverage_suffix, algorithm))


def plot_roc_curve(estimator, auc):
    """
    Plots the ROC AUC curve of a given estimator
    :param estimator: the estimator
    :param auc: the roc curve
    """

    x_train, x_test, y_train, y_test = train_test_split(X, Y,
                                                        stratify=Y,
                                                        train_size=0.8,
                                                        test_size=0.2,
                                                        shuffle=True)
    one_hot_encoder = OneHotEncoder()
    estimator.fit(x_train, y_train)
    one_hot_encoder.fit(estimator.apply(x_train))
    y_predicted = estimator.predict_proba(x_test)[:, 1]
    false_positive, true_positive, _ = roc_curve(y_test, y_predicted)

    lw = 2

    trace1 = go.Scatter(x=false_positive,
                        y=true_positive,
                        mode='lines',
                        line=dict(color='darkorange', width=lw),
                        name='ROC curve (area = %0.2f)' % auc
                        )

    trace2 = go.Scatter(x=[0, 1], y=[0, 1],
                        mode='lines',
                        line=dict(color='navy', width=lw, dash='dash'),
                        showlegend=False)

    layout = go.Layout(xaxis=dict(title='False Positive Rate',
                                  color='black'),
                       yaxis=dict(title='True Positive Rate',
                                  color='black'),
                       legend=dict(orientation="h"),
                       margin=go.Margin(l=80,
                                        r=50,
                                        b=50,
                                        t=20,
                                        pad=10))

    fig = go.Figure(data=[trace1, trace2], layout=layout)
    py.image.save_as(fig, filename='{}/roc_{}.pdf'.format(DATA_DIR, coverage_suffix))


def get_scoring():
    """Returns the scores to evaluate the model"""
    return dict(accuracy=make_scorer(accuracy_score),
                precision=make_scorer(precision_score),
                recall=make_scorer(recall_score),
                f1_score=make_scorer(f1_score),
                roc_auc_scorer=make_scorer(roc_auc_score),
                mean_absolute_error=make_scorer(mean_absolute_error),
                brier_score=make_scorer(brier_score_loss))


if __name__ == '__main__':
    pass
