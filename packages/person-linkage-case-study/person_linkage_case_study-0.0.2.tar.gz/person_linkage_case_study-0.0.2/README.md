# Person linkage case study (for PyPI)

**If you have access to GitHub, we recommend installing from https://github.com/ihmeuw/person_linkage_case_study.**
**This package is provided only for the convenience of users who cannot access GitHub.**

## Getting started

Before you start, you'll need to have Python installed.
If you intend to use Spark, you'll also need Spark **3.4** to be installed
on your system.

First, make a directory to use for development.
Inside this directory, create and enter a virtual environment for this project:

```console
$ python -m venv .venv
$ source .venv/bin/activate
```

and install this package:

```console
$ pip install person_linkage_case_study
```

Your new working directory for interacting with the case study will
be *inside this venv*. Specifically:

```console
$ cd .venv/lib/python3.*/site-packages/person_linkage_case_study
```

To test that things are set up correctly, try running:

```console
$ snakemake --forceall
```