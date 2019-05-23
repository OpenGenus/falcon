#########################
######## FALCON #########
#########################

# This serves as an installer for openfalcon

from setuptools import setup

# -e,--editable <path/url>
# Install a project in editable mode (i.e.  setuptools "develop mode") from a local project path.
setup(
    name="openfalcon",
    python_requires=">3.5.2",
    version="0.0.1",
    install_requires=["argparse", "gitpython", "pygtrie"],
    entry_points={"console_scripts": ["openfalcon=services.openfalcon:main"]},
)
