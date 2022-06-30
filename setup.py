from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in zatca_fatoora/__init__.py
from zatca_fatoora import __version__ as version

setup(
	name="zatca_fatoora",
	version=version,
	description="ZATCA Fatoora for KSA",
	author="Sowaan",
	author_email="info@sowaan.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
