#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from DAG import DAG, DAGTerm
from MeSH import MeSHDAG, MeSHTerm

import os
baseDir = os.path.dirname(os.path.abspath(__file__))
MeSHTerm.defaultMeSHDir = os.path.join(baseDir, "./Raw Data/MeSHTerm")


"""
@author: Shi4712
@description: 
@version: 1.0.0
@file: __init__.py.py
@time: 2024/6/5 16:04
"""

if __name__ == '__main__':
    pass
