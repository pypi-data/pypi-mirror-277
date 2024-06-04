from setuptools import setup, find_packages

setup(
    name='wkbk_package',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'wkbk_package=my_pkg.Hello:main',
        ],
    },
    author='WK BK',
    description='A simple package to create a hello file in the user download directory',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
