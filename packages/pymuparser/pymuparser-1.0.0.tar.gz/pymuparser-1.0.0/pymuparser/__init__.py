"""
pyMuParser |version|
====================

Overview
--------

A python binding of MuParser.

Requirements
------------

  - Python 3.8+
  - Python modules: NumPy


Installation
------------

The easiest method to install is via pip.

"""
from __future__ import absolute_import
import importlib.metadata

# Equations of state
from . import expression

__version__ = importlib.metadata.version("muparser")
