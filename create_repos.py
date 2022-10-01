from git import Repo
import os, shutil
import pathlib

rw_dir = pathlib.Path(os.getcwd()).parent
#Parse input: Firstname, Lastname, GithubName
first_name = "Alanna"
last_name = "Pasco"
github_name = "alannapasco"
repo_permissions = "admin"

#Create bare repo
repo = Repo.init(os.path.join(rw_dir, first_name+last_name), bare=True)
assert repo.bare

#Set up with unit folders/readmes in each of the folders 
example_repo = "C:/Users/jrami/VSCodeProjects/JoseRamirez"
shutil.copytree(example_repo, repo.working_dir, dirs_exist_ok=True)

#Add student as collaborator 
repo.add_to_collaborators(github_name, repo_permissions)

