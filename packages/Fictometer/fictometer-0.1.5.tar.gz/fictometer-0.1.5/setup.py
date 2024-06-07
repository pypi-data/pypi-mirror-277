from setuptools import setup, find_packages

setup(
    name = 'Fictometer',
    version = '0.1.4',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['*.sav'],
    }
)