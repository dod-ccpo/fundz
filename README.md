
# ATST

[![Build Status](https://travis-ci.org/dod-ccpo/atst.svg?branch=master)](https://travis-ci.org/dod-ccpo/atst)

## Installation

    script/setup

The setup script installs pipenv, which is what this application uses to manage its dependences and virtualenv. Instead of the classic `requirements.txt` file, pipenv uses a Pipfile and Pipfile.lock, making it more similar to other modern package managers like yarn or mix.

To enter the virtualenv manually (a la `source .venv/bin/activate`):

    pipenv shell

## Running (development)

To start the app and watch for changes:

    script/server

## Testing

To run unit tests:

    script/test

or

    python -m pytest

To run the unit tests and watch for changes to python files:

    script/test watch
