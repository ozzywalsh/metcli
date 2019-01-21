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
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Topic :: Utilities'
    ],
    keywords='weather utility cli',
    url='https://github.com/ozzywalsh/metcli',
    license='MIT',
    packages=['metcli'],
    install_requires=[
        'requests',
        'termcolor'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['metcli=metcli.command_line:main']
    },
    include_package_data=True,
    zip_safe=False
)
