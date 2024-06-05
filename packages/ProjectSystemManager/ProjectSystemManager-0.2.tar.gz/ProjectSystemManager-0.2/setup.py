from setuptools import setup, find_packages

setup(
    name='ProjectSystemManager',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'configparser',  # For parsing configuration files
        # Add any other dependencies you're using here
    ],
)