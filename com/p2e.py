#!/usr/local/bin/python2.7
# coding: utf-8

import distutils
import py2exe
import sys

if len(sys.argv) == 1: 
    sys.argv.append("py2exe") 
    sys.argv.append("-q") 
distutils.core.setup(windows=['win.py'])

