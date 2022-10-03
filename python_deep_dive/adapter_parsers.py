import pathlib
import shutil

import git
import pandas
import warnings

data = pandas.read_csv("branches.csv")

branches = list(map(str.strip, data["ids"].values.tolist()))
print(f"total branches: {len(set(branches))}")
repo_clone_url = "https://bitbucket.org/cashdash/reconciliation-reports-adapter.git"
local_repo = "recon_adapter"
results_folder = "results"

if pathlib.Path(local_repo).is_dir():
    shutil.rmtree(local_repo)

if pathlib.Path(results_folder).is_dir():
    shutil.rmtree(results_folder)

repo = git.Repo.clone_from(repo_clone_url, local_repo)

for remote in repo.remotes:
    remote.fetch()

for index, gateway_id in enumerate(branches):
    print(f"working on #{index}: {gateway_id}")
    branch_name = f"{gateway_id}-reconciliation-reports-adapter"
    repo.git.checkout(branch_name)

    new_parent_location = pathlib.Path(f"{results_folder}/{gateway_id}")
    new_parent_location.mkdir(exist_ok=True, parents=True)

    adapter_file_path = next(pathlib.Path("recon_adapter").glob("*/gatewayAdapter.py"))
    new_adapter_file_path = new_parent_location.joinpath("gatewayAdapter.py")

    shutil.copyfile(adapter_file_path, new_adapter_file_path)

    new_incoming_file_folder = new_parent_location.joinpath("incoming_data")
    new_incoming_file_folder.mkdir(exist_ok=True, parents=True)
    incoming_files_folder = pathlib.Path("recon_adapter/sourceIncomingFile")
    if not incoming_files_folder.is_dir():
        warnings.warn(f"omitting {gateway_id} incoming data file", stacklevel=2)
        continue

    for file_path in incoming_files_folder.iterdir():
        shutil.copyfile(file_path, new_incoming_file_folder.joinpath(file_path.name))
