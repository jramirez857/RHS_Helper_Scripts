from git import Repo
import os, shutil
import pathlib
repos = ["C:/Users/jrami/VSCodeProjects/JoseRamirez", "C:/Users/jrami/VSCodeProjects/AlannaPasco"]

for repo_dir in repos:
    repo = Repo(repo_dir)
    readme_file = "C:/Users/jrami/VSCodeProjects/RHS_Helper_Scripts/README.md"
    readme_filename = pathlib.Path(readme_file).name

    repo_readme = f"{repo.working_dir}/{readme_filename}"

    # Copy the file to the repo
    shutil.copy(readme_file, repo.working_dir)
    assert os.path.exists(repo_readme)

    # Add the file to the repo
    repo.index.add([readme_filename])

    # Commit the file to the repo
    repo.index.commit(f"Added {readme_filename}")

    # Push the file to the repo
    info = repo.remotes.origin.push()[0]
    print(info.flags)