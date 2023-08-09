import os
from collections import defaultdict
from datetime import datetime
from dateutil.relativedelta import relativedelta
from typing import Dict, List, Tuple

import git
import matplotlib.pyplot as plt
from git import Repo

REPO_DIR = "./neutron"
URL = "https://github.com/openstack/neutron.git"


def clone_pull_repo(repo_dir: str) -> Repo:
    """Clone repository or pull updates if it already exists"""
    if not os.path.exists(repo_dir):
        repo = git.Repo.clone_from(URL, repo_dir)
    else:
        repo = git.Repo(repo_dir)
        repo.remote().pull()
    return repo


def process_commits(repo: Repo, since: datetime) -> Dict[str, int]:
    """Iterate through all commits and count changes for every module"""
    module_commits = defaultdict(int)
    for commit in repo.iter_commits("master", since=since):
        for file in commit.stats.files:
            path_parts = file.split("/")
            if (
                len(path_parts) > 2
                and path_parts[0] == "neutron"
                and path_parts[-1].endswith(".py")
            ):
                module = path_parts[1]
                module_commits[module] += 1
    return module_commits


def plot_barchart(top_modules: List[Tuple[str, int]]) -> None:
    modules, commit_counts = zip(*top_modules)
    plt.figure(figsize=(10, 6))
    plt.bar(modules, commit_counts, color="skyblue")
    plt.xlabel("Modules")
    plt.ylabel("Number of Commits")
    plt.title("Top 5 Most Actively Changed Modules in Last 3 Years")
    plt.tight_layout()
    plt.savefig("report_chart.png")
    plt.show()


def main():
    repo = clone_pull_repo(REPO_DIR)

    three_years_ago = datetime.now() - relativedelta(years=3)
    module_commits = process_commits(repo, three_years_ago)

    top5_modules = sorted(module_commits.items(), key=lambda x: x[1], reverse=True)[:5]
    plot_barchart(top5_modules)
    for module, count in top5_modules:
        print(f"Module: {module}, Commits: {count}")


if __name__ == "__main__":
    main()
