"""
                     ___     __
 ___  ___  ___ ___  / _/__ _/ /______  ___
/ _ \/ _ \/ -_) _ \/ _/ _ `/ / __/ _ \/ _ \
\___/ .__/\__/_//_/_/ \_,_/_/\__/\___/_//_/
   /_/

This serves as an installer for openfalcon
"""

from setuptools import setup

# -e,--editable <path/url>
# Install a project in editable mode (i.e.  setuptools "develop mode") from a local project path.
setup(
    name="openfalcon",
    versio = '0.0.1',
    packages = ['services'],
    python_requires=">3.5.2",
    version="0.0.1",
    install_requires=["argparse", "gitpython", "pygtrie"],
    entry_points={"console_scripts": ["openfalcon=services.openfalcon:main"]},
)
