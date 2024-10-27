# pip/setup.py

from setuptools import setup, find_packages

setup(
    name='steamgamedata',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    description='A package to fetch and save game data from the Steam API.',
    author='NotMega',
    url='https://github.com/iamnotmega/steamgamedata',  # Update with your actual repo
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='GNU General Public License v3.0',
)