import git
import sys

__author__ = "Giovanni Grano"
__license__ = "MIT"
__email__ = "grano@ifi.uzh.ch"


def get_last_commit_id(repo_path):
    """Returns the id of the last commit for a git repository

    Arguments
    -------------
    - repo_path: the path for the repository

    """
    repo = git.Repo(repo_path + '/.git')
    last_commit = repo.head.commit
    return str(last_commit)


def main():
    repo = sys.argv[1]
    commit_id = get_last_commit_id(repo)
    print("Last commit for the project {} = {}".format(repo, commit_id))


if __name__ == '__main__':
    main()
