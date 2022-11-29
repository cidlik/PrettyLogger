from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup(
    name="PrettyLogger",
    version="1.0.0",
    description="TODO",
    packages=find_packages(where="PrettyLogger"),
    entry_points={
        "console_scripts": [
            "PrettyLogger = PrettyLogger.main:main",
        ]
    }
)
