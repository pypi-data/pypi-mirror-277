import os

import pandas as pd
from numpy import nan

from .DAG import DAGTerm, DAG


class MeSHTerm(DAGTerm):
    relationship = "children"

    def __init__(self, termSeries):
        try:
            id = termSeries["id"]
            name = termSeries["name"]
            treeNum = termSeries["treeNum"]
            childIds = termSeries["childIds"]
            abstract = termSeries["abstract"]
            uniqueId = termSeries["uniqueId"]
            synonym = termSeries["synonym"]
        except IndexError as e:
            raise IndexError("Index of term series should obtain all of"
                             "[name, comment, xref, definition, synonym, is_a, alt_id, is_obsolete]")
        childIds = childIds.split("\n") if pd.notnull(childIds) else []
        relationShipDict = {"childrenIds": childIds}
        super().__init__(id=id, name=name, relationShipDict=relationShipDict)
        self.treeNum = treeNum.split("\n")
        self.abstract = abstract
        self.uniqueId = uniqueId
        self.synonym = ([name] + synonym.split("\n")) if synonym is not nan else [name]

    @staticmethod
    def __inSameBranch(treeNumA, treeNumB):
        if treeNumA == "0" or treeNumB == "0":
            return True
        return (treeNumA in treeNumB) or (treeNumB in treeNumA)

    def returnSameBranch(self, otherTerm):
        sameBranches = []
        for treeNumA in self.treeNum:
            for treeNumB in otherTerm.treeNum:
                if self.__inSameBranch(treeNumA, treeNumB):
                    sameBranches.append(treeNumA if self.isDescendant(otherTerm) else treeNumB)
        if len(sameBranches) == 0:
            return False
        return sameBranches

    def isDescendant(self, ancestor):
        if ancestor.treeNum == ['0']:
            return True
        for ancestorTreeNum in ancestor.treeNum:
            for descendantTreeNum in self.treeNum:
                if ancestorTreeNum in descendantTreeNum:
                    return True
        return False


class MeSHDAG(DAG):
    import os
    baseDir = os.path.dirname(os.path.abspath(__file__))
    defaultMeSHDir = os.path.join(baseDir, "./Raw Data/MeSHTerm")

    @classmethod
    def returnMeSHDAG(cls, **kwargs):
        MeSHDir = kwargs.get("MeSHDir", cls.defaultMeSHDir)
        meshDf = kwargs.get("MeSHDf", None)
        if meshDf is None:
            meSHFileNameList = os.listdir(MeSHDir)
            meSHFilePathList = [os.path.join(MeSHDir, meSHFileName) for meSHFileName in meSHFileNameList]

            meshDf = pd.concat([pd.read_json(meSHFilePath, dtype={"id": str}) for meSHFilePath in meSHFilePathList])

        meshDf = meshDf.dropna(subset=["name"])
        meshDf = meshDf.drop_duplicates(keep="first", subset="id")
        meshDf.index = range(0, len(meshDf))

        # 2024 已纠正
        # meshDf.loc[meshDf["id"] == "68054988", "childIds"] = "68018549"  # 存在 Idiopathic Pulmonary Fibrosis --> Idiopathic Interstitial Pneumonias --> Idiopathic Pulmonary Fibrosis 死循环

        meshDf.loc[meshDf["id"] == "68013285", "childIds"] = "68004948\n68005099\n68004948\n68005099"  # 存在 Ocular Motility Disorders --> Strabismus --> Ocular Motility Disorders 死循环

        meshDf["term"] = meshDf.T.apply(lambda termSeries: MeSHTerm(termSeries))
        meshDf["term"].apply(lambda term: term.setTermFromDf(termDf=meshDf, idColName="id", termsColName="term"))
        rootIndex = meshDf.loc[meshDf["name"] == "All MeSH Categories"].index.tolist()[0]
        meshTermDAG = MeSHDAG(meshDf.loc[rootIndex, "term"], meshDf["term"])
        return meshTermDAG

    def __init__(self, root, termSeries, termsIndexName="name", get_sub=False):
        super().__init__(root, termSeries, termsIndexName, get_sub)


def worker(namespace):
    print(namespace.obj.root)


if __name__ == "__main__":
    # simMeSH = [
    #     ["000", "root", "0", "001\n002\n003", "The root of simulative MeSH", "000", nan],
    #     ["001", "1", "0.1", "004", "0->1->4", "001", nan],
    #     ["002", "2", "0.2", "004\n005", "0->2->4;0->2->5", "002", nan],
    #     ["003", "3", "0.3", "007", "0->3->7", "003", "???"],
    #     ["004", "4", "0.1.4\n0.2.4", "006\n008", "0->1->4-;0->2->4->6;0->2->4->8", "004", nan],
    #     ["005", "5", "0.2.5", "006", "0->2->5->6", "005", nan],
    #     ["006", "6", "0.2.4.6\n0.2.5.6", nan, "0->2->4->6->None;0->2->5->6->None", "006", nan],
    #     ["007", "7", "0.3.7", nan, "0->3->7->None", "007", nan],
    #     ["008", "8", "0.2.4.8", nan, "0->2->4->8->None", "008", nan],
    # ]
    # columns = ["id", "name", "treeNum", "childIds", "abstract", "uniqueId", "synonym"]
    # meshDf = pd.DataFrame(simMeSH, columns=columns)
    # # meshTermDAG = MeSHDAG.returnMeSHDAG(meshDf=meshDf)
    # meshDf["term"] = meshDf.T.apply(lambda termSeries: MeSHTerm(termSeries))
    # meshDf["term"].apply(lambda term: term.setTermFromDf(termDf=meshDf, idColName="id", termsColName="term"))
    # meshTermDAG = MeSHDAG(meshDf.loc[0, "term"], meshDf["term"])
    # (testTerm_6, testTerm_2, testTerm_1) = meshTermDAG.getTerms(["6", "2", "1"])
    # print(testTerm_6.returnSameBranch(testTerm_2))
    # print(testTerm_6.isDescendant(testTerm_2))
    # print(testTerm_6.isDescendant(testTerm_1))
    # print(testTerm_6.isDescendant(meshTermDAG.root))
    # print("Test has been done successfully")

    meshTermDAG = MeSHDAG.returnMeSHDAG(MeSHDir=os.path.join(baseDir, "./Raw Data/MeSHTerm"))

    from multiprocessing import Process, Manager

    with Manager() as manager:
        namespace = manager.Namespace()
        namespace.obj = meshTermDAG  # Put MyClass instance into Namespace

        p = Process(target=worker, args=(namespace,))
        p.start()
        p.join()

        print(namespace.obj.root.name)  # Should print "1"

