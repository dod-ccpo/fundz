
# fundz

[![Build Status](https://travis-ci.org/dod-ccpo/fundz.svg?branch=master)](https://travis-ci.org/dod-ccpo/fundz)

## Installation

### Cloning
This project contains git submodules. Here is an example clone command that will
automatically initialize and update those modules:

    git clone --recurse-submodules git@github.com:dod-ccpo/fundz.git

If you have an existing clone that does not yet contain the submodules, you can
set them up with the following command:

    git submodule update --init --recursive

### Setup

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

## Direnv

If you're using direnv, refer to ![this page](https://github.com/direnv/direnv/wiki/Python#-pipenv).

## Environment Variables

`ENVIRONMENT`: Maps to `FLASK_ENV`. Can be either `development` or `production`.
`DEBUG`: Enable debug mode.
`DATABASE_URI`: The full database connection string.
