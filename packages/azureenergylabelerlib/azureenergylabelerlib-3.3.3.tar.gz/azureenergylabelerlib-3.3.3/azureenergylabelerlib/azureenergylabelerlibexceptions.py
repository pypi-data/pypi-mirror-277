#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: azureenergylabelerlibexceptions.py
#
# Copyright 2022 Sayantan Khanra
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.
#

"""
Custom exception code for azureenergylabelerlib.

.. _Google Python Style Guide:
   https://google.github.io/styleguide/pyguide.html

"""

__author__ = '''Sayantan Khanra <skhanra@schubergphilis.com>'''
__docformat__ = '''google'''
__date__ = '''22-04-2022'''
__copyright__ = '''Copyright 2022, Sayantan Khanra'''
__credits__ = ["Sayantan Khanra"]
__license__ = '''MIT'''
__maintainer__ = '''Sayantan Khanra'''
__email__ = '''<skhanra@schubergphilis.com>'''
__status__ = '''Development'''  # "Prototype", "Development", "Production".


class InvalidSubscriptionListProvided(Exception):
    """The list of subscriptions provided are not valid Azure subscriptions."""


class MutuallyExclusiveArguments(Exception):
    """The arguments provided are mutually exclusive and only one of the should be provided."""


class SubscriptionNotPartOfTenant(Exception):
    """If subscription ids are provided but are not part of the tenant."""


class InvalidCredentials(Exception):
    """Credentials provided are not valid."""


class InvalidFrameworks(Exception):
    """The frameworks provided are not valid."""


class InvalidPath(Exception):
    """The path provided is not valid."""


class InvalidResourceGroupListProvided(Exception):
    """The provided list of resource groups names are not valid Azure resource groups names."""
