#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Shi4712
@description: 
@version: 1.0.0
@file: DAGTest.py
@time: 2024/6/6 9:07
"""

if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    from numpy import nan, inf
    from bioDAG import DAG, DAGTerm

    simDAG = [
        ["000", "root", "001\n002\n003", "The root of simulative MeSH"],
        ["001", "1", "004", "0->1->4"],
        ["002", "2", "004\n005", "0->2->4;0->2->5"],
        ["003", "3", "007", "0->3->7"],
        ["004", "4", "006\n008", "0->1->4-;0->2->4->6;0->2->4->8"],
        ["005", "5", "006", "0->2->5->6"],
        ["006", "6", nan, "0->2->4->6->None;0->2->5->6->None"],
        ["007", "7", nan, "0->3->7->None"],
        ["008", "8", nan, "0->2->4->8->None"],
    ]
    columns = ["id", "name", "childIds", "abstract"]
    DAGDf = pd.DataFrame(simDAG, columns=columns)
    DAGDf["term"] = DAGDf.T.apply(lambda termSeries: DAGTerm(
        id=termSeries["id"], name=termSeries["name"],
        relationShipDict={
            "childrenIds": termSeries["childIds"].split("\n") if termSeries["childIds"] is not nan else []}
    ))
    DAGDf["term"].apply(lambda term: term.setTermFromDf(termDf=DAGDf, idColName="id", termsColName="term"))
    dagDAG = DAG(DAGDf.loc[0, "term"], DAGDf["term"], termsIndexName="name")
