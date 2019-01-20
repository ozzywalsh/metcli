import setuptools


setuptools.setup(
    name='metcli',
    author='Ozzy Walsh',
    description="A cli interface to Met Eireann",
    install_requires=[
        'requests',
        'termcolor'
    ],
    entry_points={
        'console_scripts': ['metcli=metcli.command_line:main']
    }
)
