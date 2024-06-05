#!/usr/bin/env python
import os

from setuptools import setup

if __name__ == "__main__":

    base_dir = os.path.dirname(__file__)
    src_dir = os.path.join(base_dir, "person_linkage_case_study", "src")

    with open(os.path.join(base_dir, "README.md")) as f:
        long_description = f.read()

    setup_requires = ["setuptools_scm"]

    install_requirements = [
        # Core libraries
        "pandas",
        "pyarrow",
        "numpy",
        "matplotlib",
        "pseudopeople",
        "splink",
        "jellyfish",
        # Workflow management and headless Jupyter
        "snakemake",
        "papermill",
        "ipython",
        "ipykernel",
        # Pins
        "pulp<2.8",  # Needed for snakemake, see https://github.com/snakemake/snakemake/issues/2607#issuecomment-1948732242
    ]
    dask_requirements = [
        "pseudopeople[dask]",
        "dask_jobqueue",
        "bokeh!=3.0.*,>=2.4.2",  # needed for dask dashboard
    ]
    spark_requirements = [
        "pyspark==3.4.1",  # NOTE: I have no idea why, but pyspark 3.5.0 (with the correct version of Spark) would hang forever on the first stage
    ]
    dev_requirements = (
        [
            "jupyterlab",
            "nbdime",
            "black[jupyter]",
        ]
        + dask_requirements
        + spark_requirements
    )

    setup(
        name="person_linkage_case_study",
        description="Person linkage case study for PyPI.",
        long_description=long_description,
        license="BSD-3-Clause",
        url="https://github.com/ihmeuw/person_linkage_case_study",
        author="IHME Simulation Science Team",
        author_email="zmbc@uw.edu",
        package_dir={
            "person_linkage_case_study": "person_linkage_case_study",
            "person_linkage_case_study_utils": "person_linkage_case_study/src/person_linkage_case_study_utils",
        },
        packages=["person_linkage_case_study", "person_linkage_case_study_utils"],
        package_data={
            "person_linkage_case_study": [
                "benchmarks/**/*",
                "config/**/*",
                "data/**/*",
                "diagnostics/**/*",
                "profiles/**/*",
                "spark_slurm_container/**/*",
                "*.ipynb",
                "LICENSE",
                "README.md",
                "Snakefile",
                "*.txt",
            ],
        },
        install_requires=install_requirements,
        extras_require={
            "dask": dask_requirements,
            "spark": spark_requirements,
            "dev": dev_requirements,
        },
        zip_safe=False,
        use_scm_version={
            "tag_regex": r"^(?P<prefix>v)?(?P<version>[^\+]+)(?P<suffix>.*)?$",
        },
        setup_requires=setup_requires,
    )
