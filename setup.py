#
#                     ___     __
# ___  ___  ___ ___  / _/__ _/ /______  ___
#/ _ \/ _ \/ -_) _ \/ _/ _ `/ / __/ _ \/ _ \
#\___/ .__/\__/_//_/_/ \_,_/_/\__/\___/_//_/
#   /_/
#
#This serves as an installer for openfalcon
#

from setuptools import setup, find_packages

# -e,--editable <path/url>
# Install a project in editable mode (i.e.  setuptools "develop mode") from a local project path.
setup(
    name='openfalcon',
    version='0.0.1',
    description='Falcon is a library which allows you to use the Cosmos library in a convenient way.',
    author='Opengenus Foundation',
    author_email='team@opengenus.org',
    url='https://github.com/OpenGenus/falcon',
    python_requires='>3.5.2',
    install_requires=['argparse', 'gitpython', 'pygtrie'],
    entry_points={'console_scripts': ['openfalcon=services.openfalcon:main']},
    include_package_data=True,
    packages = ['.']
)
