|
--------------------------------------------- |
hackoregon_test |

[![image](<https://badge.fury.io/py/>2019-test-backend.svg)](<https://badge.fury.io/py/>2019-test-backend)

[![image](<https://travis-ci.org/hackoregon/>2019-test-backend.svg?branch=master)](<https://travis-ci.org/hackoregon/>2019-test-backend)

This is just to test the Backend Django Cookiecutter repo before teaching other people on it.

# Documentation

The full documentation is at <<http://hackoregon.github.io/>>2019-test-backend

# Features

> -   TODO (add what your project does)

# Data Sources

# Quickstart to install package in your own Django Project (Non-Hack
Oregon Workflow)

Install hackoregon_test:

> pip install hackoregon_test

Add subpackages to your `INSTALLED_APPS`:

`` ` python INSTALLED_APPS = (     ...     'tester',     ... ) ```

Add hackoregon_test's URL patterns:

`` ` python from hackoregon_test.tester import urls as tester_urls   urlpatterns = [     ...     url(r'^', include(tester_urls)),     ... ] ```

Setup your database with a matching schema

Run the project

# Running Tests

This repo uses pytest and pytest-django to run tests.

For project development work, tests will be run in docker container
using the bin/test.sh script:

# Credits

Tools used in rendering this package:

> -   [Cookiecutter](<https://github.com/audreyr/cookiecutter>)
> -   [cookiecutter-djangopackage](<https://github.com/pydanny/cookiecutter-djangopackage>)
