import setuptools

# read the contents of the README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(
    name='metcli',
    version='0.1.0',
    author='Ozzy Walsh',
    description='A command line interface for Met Éireann.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    install_requires=[
        'requests',
        'termcolor'
    ],
    entry_points={
        'console_scripts': ['metcli=metcli.command_line:main']
    }
)
