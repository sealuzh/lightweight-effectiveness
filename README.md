# Replication Package 

In this replication package we make available **every** single script needed to **fully** replicate the results obtained in our paper.

## Requirements

* Java 1.8
* Maven 
* Python 3

One you install everything, you can use the following command to install every Python package.

`pip install -r requirements.txt`

## Steps

Export the `PYTHONPATH` variable with the command `export PYTHONPATH=$(pwd)`.

At first, the projects used for the evaluation need to be locally cloned.

```
python effectiveness/runner.py projects.csv clone
chmod 777 get_projects.sh
./get_projects.sh
```

Then, you can generate the scripts used to perform the mutation testing and then execute it.

```
python effectiveness/runner.py projects.csv run
chmod 777 run_experiment.sh
./run_experiment.sh
```

Please be **aware** that the entire process will take several hours. It is convenient to run it on a powerful dedicated server.

At the end of the mutation experiment, you have to aggregate the values for the obtained scores with:

```
python effectiveness/mutation/calcolate_results.py
```

After that, the command 
```
python effectiveness/mutation/aggregate_source.py
```
will merge in an unique frame the several metrics computed with third party tools. Please note that we provide those metrics pre-calculated since the employed tool are research prototypes not yet published!

This process will save in your DATA directory two csv files with the all the data needed for the classifier.

At the end, executing 
```
python effectiveness/classification.py
```
you will train and evaluate the machine learning classifier.
Please note that also this step takes a considerable amount of time.

The `main` method of the `classification.py` file runs the nested cross-validation pipeline that returns and save the results only for the best algorithm. 
In the case you are interested in singularly run one algorithm at time, use the `classification(consider_coverage, n_inner, n_outer, algorithm)` with an a specified argument for `algorithm`.

For instance, running
`classification(consider_coverage=True, n_inner=5, n_outer=10, algorithm=svc)`
will train a SVC classifier using also the line coverage with a 5-k inner and a 10-k outer cross-fold validation.

## Docker image
We provide also a Dockerfile that can be used to build an image to replicate the results. Please note that, since you will create a Ubuntu image, you have to specify `python3` instead of the usual `python` (with is the version 2.7 by default)

## Full Results

The full results about the accuracy of the 3 experimented algorithms are available in the [this](https://github.com/sealuzh/lightweight-effectiveness/tree/master/data) directory.
The _dynamic_ suffix indicate the model trained with the line coverage metric, while the _static_ one imply only static metrics. The last suffix indicates the algorithm used, i.e., _rfc_ for Random Forest, _knn_ for K-Nearest Neighbors and _scv_ for Support Vector Classifier.

## Metrics Extracted
All the files with the metric values are available in [this](https://github.com/sealuzh/lightweight-effectiveness/tree/master/metrics) directory.

## Projects
We also share the list of the 18 projects used in the study, along with the commit used [here](https://github.com/sealuzh/lightweight-effectiveness/tree/master/projects)

## Metrics Used
A detailed list of the metrics used in this work is reported at this [link](https://github.com/sealuzh/lightweight-effectiveness/blob/master/metrics.md) or, alternatively, in the wiki page of this repository.

## Tool Versions 
In this work we rely on the following tools:

* PIT version 1.3.2
* sciknit version 0.19.1
* Maven version 3.5.0
* Python version 3.6.4
