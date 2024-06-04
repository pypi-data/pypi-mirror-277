from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
	name="tmp_box",
	version="0.0.7",
	packages=find_packages(),
	include_package_data=True,
	install_requires=[
		"typer>=0.12.3",
		"pydantic>=2.7.2"
	],
	entry_points={
		"console_scripts": [
			"tmp-box = app.main:app"
		]
	},
	package_data={'app': ['repositories/json_dir/*.json']}
)
