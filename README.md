# Readme

[![Python: 3.8](https://img.shields.io/badge/python-3.8-b58900.svg)](https://docs.python.org/3/whatsnew/3.8.html)
[![Test: pytest](https://img.shields.io/badge/test-pytest-93a1a1.svg)](https://github.com/pytest-dev/pytest)
[![Style: black](https://img.shields.io/badge/style-black-002b36.svg)](https://github.com/python/black)
[![Style: isort](https://img.shields.io/badge/style-isort-2aa198.svg)](https://github.com/timothycrosley/isort)
[![Lint: flake8](https://img.shields.io/badge/lint-flake8-6c71c4.svg)](https://github.com/PyCQA/flake8)
[![Typing: mypy](https://img.shields.io/badge/typing-mypy-d33682.svg)](https://github.com/python/mypy)
![License: proprietary](https://img.shields.io/badge/license-proprietary-cb4b16.svg)

## `his-geo-backend`

his-geo-backend

## Development Environment

We use [conda](https://conda.io/) as a package and environment manager.

1. Create an environment that includes `python` and `invoke`.
2. Activate the environment.
3. Install required packages with `bootstrap`.
4. Install this package in `develop` mode.
5. Install [git](https://git-scm.com/) `hooks`.
6. List available tasks.

```sh
$ conda create -n his-geo-backend python=3.8.10 invoke --yes
$ conda activate his-geo-backend
$ invoke bootstrap develop hooks
$ invoke --list
```

## Check

We use various utilities to check coding style and to check for errors with static typing.

* [flake8](http://flake8.pycqa.org/) to make a first-pass at enforcing style rules.
* [isort](https://timothycrosley.github.io/isort/) to deterministically sort python imports.
* [black](https://black.readthedocs.io/) to make a final-pass at enforcing style rules.
* [mypy](http://www.mypy-lang.org/) to use static type checking to prevent errors.

```sh
$ invoke check
```

To have some of these tools try to automatically fix errors, use `invoke format`. Output is best-effort and may not be
optimal.

## Push

Changes must be [pushed](https://git-scm.com/docs/git-push) to a branch, and a pull request must be created for commits
to be merged into master. Only after a peer code review and successful builds can the pull request can be merged. To
ensure that we don't waste time and resources, we use a
[pre-push hook](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) to run checks and tests before a push. If
tests run quickly, we increase productivity and decrease waste with little cost. To
[bypass the pre-push hook](https://git-scm.com/docs/git-push#Documentation/git-push.txt---no-verify), use `--no-verify`.

## Release

We use [git tag](https://git-scm.com/book/en/v2/Git-Basics-Tagging) and CI to automatically generate releases.

1. Display what `releases` are already available.
2. Generate a new `release`.

```sh
$ invoke releases
$ invoke release 1.0.0
```

When you generate a release, a URL will be provided to follow the build's progress.

## Versions

Production version numbers must follow a standard `x.y.z` format. Non-production version numbers should use the same
format, but include a pre-release suffix such as `a` (alpha), `b` (beta), or `rc` (release candidate).

### Examples

| Version    | Style       |
|------------|-------------|
| `1.0.0a1`  | Development |
| `1.0.0b3`  | Development |
| `1.0.0rc2` | Development |
| `1.0.0`    | Production  |