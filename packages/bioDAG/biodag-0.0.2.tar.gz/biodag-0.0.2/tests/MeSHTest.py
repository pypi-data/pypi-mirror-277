#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Shi4712
@description: 
@version: 1.0.0
@file: MeSHTest.py
@time: 2024/6/6 9:14
"""

if __name__ == '__main__':
    from bioDAG.MeSH import MeSHDAG, MeSHDAGTerm
    meshTermDAG = MeSHDAG.returnMeSHDAG()
    print(meshTermDAG)
