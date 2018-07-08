import pandas as pd
import os


def process_results(frame='results.csv', project_frame='projects.csv'):
    """Processes the results, computing some statistics:
        -  at first, discards the empty rows;
        - then it computes the

    Arguments
    -------------
    - frame: the results
    """
    if os.path.exists(frame):
        print("* Processing {}".format(frame))
    else:
        print("* No {} to process".format(frame))
        exit(0)
    frame = pd.read_csv(frame)

    # computes and store the versions used
    projects = pd.unique(frame.project)
    commits = pd.unique(frame.commit)
    version_used = pd.DataFrame({'commit': pd.Series(commits),
                                 'project': pd.Series(projects)})
    output_replication(version_used, project_frame)

    # compute some stats
    print("* Investigated pairs = {}".format(len(frame)))
    frame = frame.dropna()
    no_classes = len(frame)
    print("* Removing NaN pairs = {}".format(no_classes))
    print("* Quantiles\n-------------")
    quantiles = frame.quantile([0.25, 0.5, 0.75, 1])
    print(quantiles)
    print("\n-------------\n* Average")
    print(frame.mutation.mean())
    print("* Median")
    print(frame.mutation.median())

    print("\n-------------\n* Mutations")
    total_mutants = frame.no_mutations.sum()
    print("* Total number of mutants = {}".format(total_mutants))
    print("* Average mutant per class = {}".format(total_mutants/no_classes))


def output_replication(frame, projects):
    """Saves in output a csv with the commits analyzed for the experiment (for reproducibility)

    Arguments
    -------------
    - frame: the results

    """
    projects = pd.read_csv(projects).project.tolist()

    git_link = 'git clone https://github.com/'
    frame['clone_link'] = frame.apply(lambda x: [git_link + i for i in projects if i.endswith(x.project)][0], axis=1)
    frame.to_csv('commits.csv', index=False)


if __name__ == '__main__':
    process_results()
