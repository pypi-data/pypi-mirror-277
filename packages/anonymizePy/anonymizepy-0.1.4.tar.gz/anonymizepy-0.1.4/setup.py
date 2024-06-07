from setuptools import setup, find_packages

setup(
    name="anonymizePy",
    version="0.1.4",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.9.3",
        "pandas>=2.1.1",
        "regex>=2023.10.3",
        "spacy>=3.4.4",
        "scikit-learn>=0.24.0"
    ],
    entry_points={
        "console_scripts": [
            "anonymizePy=anonymizePy:main",
        ],
    },
)