# ai-python-common
A common repository for shared python code used within AI/ML projects

## Development

The following section details local development setup for this python package.

### Pre-Requisites

You will need the following tools setup on your computer

* [Visual Studio Code](https://code.visualstudio.com/)
* [Rancher Desktop](https://rancherdesktop.io/) for running docker
* [devcontainers vscode extension](https://code.visualstudio.com/docs/devcontainers/containers)

### Developing a feature

Once you have all the pre-requisites configured, you can open this project folder within vscode and it will prompt you to open the project inside a container. Choose "yes" to proceed.

**NOTE: The first time you open this project in container vscode will build all the container layers. This could take some time, so please be patient**

Open a new terminal and you will be connected to the container. You can now use your standard git workflow to create a new branch and start updating code.

#### Enable pre-commit hook

Enable pre-commit hook to run all configured hooks

```bash
make setup

# sample output
No dependencies to install or update

Installing the current project: i11-ai (0.1.0)
pre-commit installed at .git/hooks/pre-commit
```

#### Running Tests

Use the `Makefile` to run tests

```bash
make test

# sample output
Installing dependencies from lock file

No dependencies to install or update

Installing the current project: i11-ai (0.1.0)
pre-commit installed at .git/hooks/pre-commit
======================================================================= test session starts =======================================================================
platform linux -- Python 3.11.9, pytest-8.2.2, pluggy-1.5.0
rootdir: /workspaces/ai-python-common
configfile: pyproject.toml
collected 1 item

tests/common_test.py .                                                                                                                                      [100%]

======================================================================== 1 passed in 0.02s ========================================================================
```

## Release

* Create a new feature branch
* Bump the version number in [pyproject.toml](./pyproject.toml) file
* Update [CHANGELOG](./CHANGELOG.md) with relevant updates
* Create a new new PR and review with team
* Once PR is approved, merge the PR to `main` branch that will trigger a build to publish the package to [PyPi](https://pypi.org/project/i11-ai)
