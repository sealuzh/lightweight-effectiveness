from sklearn.externals import joblib
import numpy as np
import pandas as pd
from effectiveness.settings import *
from effectiveness.classification.classifier import import_frame
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix


def predict(coverage=False):
    """
    Predicts the output and the probabilities for each class in our dataset training a new model for each class
    """
    frame, _ = import_frame(coverage)
    class_list = frame['class_name'].tolist()
    predictions = []
    probabilities = []
    for cl in class_list:
        prediction, probability = train_and_predict_for_class(cl, coverage)
        predictions.append(prediction)
        probabilities.append(probability)
    frame['prediction'] = predictions
    frame['probability'] = probabilities
    prefix = 'dynamic' if coverage else 'static'
    frame.to_csv('{}/predictions-{}.csv'.format(DATA_DIR, prefix), index=False)


def train_and_predict_for_class(target, coverage=True, verbose=False):
    """
    Trains a new model with the best configuration reached by the nested CV validation (obtained statically)
    without using the targeted class as a training example, for a fair prediction probability
    :param target: the class name that needs to be predicted
    :param coverage: the flag for a static or dynamic model
    :return a tuble with prection and probability
    """
    frame, metrics = import_frame(coverage)
    original_shape = int(frame.shape[0])
    target_frame = frame[frame['class_name'] == target]
    frame = frame[frame['class_name'] != target]
    aux_prediction = np.nan
    aux_probability = np.nan
    if int(frame.shape[0]) < original_shape:
        model = get_model(coverage)
        model.fit(frame[metrics], frame['y'])
        aux_prediction = model.predict(target_frame[metrics])
        aux_probability = model.predict_proba(target_frame[metrics])
        if verbose:
            print('Prediction for class {}'.format(target))
            print('Output = {}'.format(aux_prediction))
            print('Probability = {}'.format(aux_probability))
    else:
        print('Something wrong with the filtering for class {}'.format(target))
        exit()
    prediction = aux_prediction[0]
    probability = aux_probability[0][0] if prediction == 0 else aux_probability[0][1]
    return prediction, probability


def get_model(coverage):
    """
    Returns the model configuration that we found be the best
    :param coverage: flag for dynamic or static configuration
    :return: the model
    """
    if coverage:
        return RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
                                      max_depth=15, max_features=60, max_leaf_nodes=None,
                                      min_impurity_decrease=0.0, min_impurity_split=None,
                                      min_samples_leaf=2, min_samples_split=2,
                                      min_weight_fraction_leaf=0.0, n_estimators=21, n_jobs=1,
                                      oob_score=False, random_state=None, verbose=0,
                                      warm_start=False)
    else:
        return RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
                                      max_depth=10, max_features=46, max_leaf_nodes=None,
                                      min_impurity_decrease=0.0, min_impurity_split=None,
                                      min_samples_leaf=2, min_samples_split=2,
                                      min_weight_fraction_leaf=0.0, n_estimators=30, n_jobs=1,
                                      oob_score=False, random_state=None, verbose=0,
                                      warm_start=False)


def check_false_and_true_positive():
    mode = ['static', 'dynamic']
    for m in mode:
        print('\n\nAnalysis for {} model'.format(m))
        path = '{}/predictions-{}.csv'.format(DATA_DIR, m)
        if os.path.exists(path):
            frame = pd.read_csv(path)
            oracle = frame['y']
            prediction = frame['prediction']
            tn, fp, fn, tp = confusion_matrix(oracle, prediction).ravel()
            print('True Positive = {}'.format(tp))
            print('False Positive = {}'.format(fp))
            print('True Negative = {}'.format(tn))
            print('False Positive = {}'.format(fn))
        else:
            print('run the prediction first')


if __name__ == '__main__':
    # target = 'com.dianping.cat.report.page.app.task.AppDatabasePruner'
    target = 'com.puppycrawl.tools.checkstyle.checks.coding.IllegalTypeCheck'
    check_false_and_true_positive()
    # print('Dynamic')
    # predict(coverage=True)
    # print('Static')
    # predict(coverage=False)
    # train_and_predict_for_class(target)
    # train_and_predict_for_class(target, coverage=False)
