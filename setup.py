from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in wwerptheme/__init__.py
from wwerptheme import __version__ as version

setup(
	name="wwerptheme",
	version=version,
	description="Wwerp Custom theme",
	author="sgatechsolutions",
	author_email="abayomi.awosusi@sgatechsolutions.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
