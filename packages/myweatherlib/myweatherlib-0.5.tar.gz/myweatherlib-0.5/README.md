# My Weather Library

This is a simple Python library for fetching and parsing weather data using the OpenWeatherMap API.

## Installation

You can install this package using pip:

```bash
pip install myweatherlib

pip install myweatherlib --index-url https://__token__:glpat-PGhPeztfJc2dQDW3WxMJ@git.e-science.pl/api/v4/projects/1030/packages/pypi/simple

python setup.py sdist bdist_wheel

twine upload --repository gitlab dist/* --verbose