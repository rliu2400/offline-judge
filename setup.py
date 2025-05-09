# setup.py
from setuptools import setup, find_packages

setup(
    name="offline-judge",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "click>=8.0",
        "requests>=2.0",
        "beautifulsoup4>=4.0",
        "tqdm>=4.0",
    ],
    entry_points={
        "console_scripts": [
            "oj=offline_judge.cli:cli",
        ],
    },
)
