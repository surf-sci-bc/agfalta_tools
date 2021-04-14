"""Setup script."""
# pylint: disable=invalid-name

from setuptools import setup, find_packages


setup(
    name="agfalta",
    use_scm_version={
        "root": ".",
        "relative_to": __file__,
        "fallback_version": "NOT-INSTALLED-VERSION"
    },
    author="Simon Fischer, Lars Buß, Jon-Olaf Krisponeit",
    description="LEEM data analysis (and more...?)",
    packages=find_packages(include=["agfalta", "agfalta.*"]),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Physics"
    ),
    # license="GPLv3",
    keywords="physics LEEM microscopy spectroscopy",
    setup_requires=["setuptools_scm"],
    install_requires=[
        "numpy",
        "matplotlib",
        "pandas",
        "scikit-learn",
        "scikit-image",
        "scikit-video",
        "pyclustering",
        "nltk",
        "opencv-python<4.0",
        "opencv-contrib-python<4.0",
        "kneed",
        "lmfit",
        "ipython",
        "netCDF4",
        "setuptools_scm",       # see agfalta/version.py
    ],
    # dependency_links=['https://github.com/annoviko/pyclustering/tarball/master'],
    package_data={"agfalta.xps": ["rsf.db"]},
    python_requires="~=3.6",
    tests_require=["pytest"]
)
