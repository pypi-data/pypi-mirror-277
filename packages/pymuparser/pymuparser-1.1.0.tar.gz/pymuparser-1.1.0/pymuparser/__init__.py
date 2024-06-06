"""
pyMuParser |version|
====================

Overview
--------

A python wrapper around MuParser.

Requirements
------------

  - Python 3.8+
  - Python modules: NumPy


Installation
------------



"""
from __future__ import absolute_import
import importlib.metadata

# Equations of state
from . import expression

__version__ = importlib.metadata.version("muparser")
