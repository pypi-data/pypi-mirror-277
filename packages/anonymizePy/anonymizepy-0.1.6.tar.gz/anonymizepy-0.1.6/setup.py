from setuptools import setup, find_packages

setup(
    name="anonymizePy",
    version="0.1.6",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "anonymizePy": [
            "resources/src/firstnames_list.txt",
            "resources/src/lastnames_list.txt",
            "resources/ignore_list.txt",
            "resources/lane_streets.txt",
            "resources/states_list.txt"
        ],
    },
    install_requires=[
        "numpy>=1.9.3",
        "pandas>=2.1.1",
        "regex>=2023.10.3",
        "spacy>=3.4.4",
        "scikit-learn>=0.24.0",
    ],
    entry_points={
        "console_scripts": [
            "anonymizepy=anonymizePy:main",
        ],
    },
)