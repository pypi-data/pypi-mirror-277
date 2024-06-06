import pandas as pd
import numpy as np
from numpy import nan, inf
import networkx as nx


class ExistsError(Exception):
    pass


class DAGTerm(object):
    missingTerms = []
    relationship = ""

    def __init__(self, id, name, relationShipDict):
        self.id = str(id)
        self.name = str(name)
        self.children = []
        self.parents = []
        if not isinstance(relationShipDict, dict):
            raise ExistsError("relationShipDict should be a dict data!!!")
        if self.relationship == "" and "childrenIds" in relationShipDict:
            self.__setRelationship("children")
        elif "parentsIds" in relationShipDict:
            self.__setRelationship("parents")
        if "childrenIds" not in relationShipDict and "parentsIds" not in relationShipDict:
            raise ExistsError("Term has no relationship of children or parents!!!")
        self.childrenIds = relationShipDict.get("childrenIds", [])
        self.parentsIds = relationShipDict.get("parentsIds", [])
        self.synonym = relationShipDict.get("synonym", [])

        self.depth = 0

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    @classmethod
    def __setRelationship(cls, relationship):
        cls.relationship = relationship

    def setTermFromDf(self, termDf, idColName, termsColName):
        if self.relationship not in ["children", "parents"]:
            raise ExistsError("The attribute of DAGTerm.relationship should be set as 'children' or 'parents'!!!")
        attrName = self.relationship
        idAttrName = "{}Ids".format(attrName)

        relationshipIds = self.__getattribute__(idAttrName)
        if relationshipIds is not nan:
            for relationshipId in relationshipIds:
                relationship = termDf[termsColName].loc[termDf[idColName] == relationshipId].to_list()
                if len(relationship) == 0:
                    self.missingTerms.append([self.id, relationshipId])
                    continue
                if len(relationship) > 1:
                    raise ExistsError("There are duplicated id in {}".format(relationshipId))
                relationship = relationship[0]
                if relationship not in self.__getattribute__(attrName):
                    if attrName == "children":
                        self.children.append(relationship)
                        relationship.parents.append(self)
                        relationship.parentsIds.append(self.id)
                    else:
                        self.parents.append(relationship)
                        relationship.children.append(self)
                        relationship.childrenIds.append(self.id)

    def getDepth(self):
        if self.depth == 0:
            self.setDepth()
        return self.depth

    def setDepth(self):
        if not self.parents:
            self.depth = 0
        else:
            self.depth = max([parent.getDepth() for parent in self.parents]) + 1

    def isChild(self, parent):
        if self == parent or self in parent.children:
            return True
        return False

    def isDescendant(self, ancestor):
        if self.depth < ancestor.depth:
            return False
        if self.isChild(ancestor):
            return True
        for child in ancestor.children:
            if self.isDescendant(child):
                return True
        return False

    def getTermsByChildDepth(self, childDepth, includeSelf=False, includeInterNode=True):
        if childDepth == -1:
            childDepth = inf
        if childDepth > 1:
            childTerms = [self] if includeSelf else []
            for child in self.children:
                childTerms += child.getTermsByChildDepth(childDepth-1)
                if includeInterNode:
                    childTerms += [child]
            return list(set(childTerms))
        return [self] + self.children if includeSelf else self.children

    def returnAncestorListWithDepth(self, depth):
        if depth > self.depth:
            raise ExistsError("{}'s ancestor depth should less than {}".format(self.name, self.depth))
        if depth == self.depth:
            return [self]
        AncestorList = []
        for parent in self.parents:
            if depth <= parent.depth:
                AncestorList += parent.returnAncestorListWithDepth(depth)
        return list(set(AncestorList))

    @classmethod
    def returnMissingDf(cls):
        missingTermDf = pd.DataFrame(cls.missingTerms, columns=["parent", "child"])
        missingTermDf = missingTermDf.drop_duplicates(keep="first")
        missingTermDf.index = range(0, len(missingTermDf))
        return missingTermDf


class DAG(object):
    missingTermDict = {}

    def __init__(self, root, termSeries, termsIndexName, get_sub=False):
        self.root = root
        self.num = len(termSeries)
        self.terms = termSeries
        self.termsIndexName = termsIndexName
        if termsIndexName == "name":
            self.terms.index = self.terms.apply(lambda x: x.name)
        else:
            self.terms.index = self.terms.apply(lambda x: x.id)
        if not get_sub:
            self.terms.apply(lambda term: term.setDepth())
        self.level = termSeries.apply(lambda x: x.depth).max() - termSeries.apply(lambda x: x.depth).min() + 1

    def getTerm(self, term):
        if isinstance(term, DAGTerm):
            if term.name in self.terms:
                term = term.name
            else:
                raise ExistsError("{} not in {}".format(term.name, self))
        elif isinstance(term, (list, set, pd.Series)) and len(term) == 1:
            term = list(term)[0]
            return self.getTerm(term)
        elif isinstance(term, str):
            pass
        else:
            raise ExistsError("Unexpect term: {}".format(term))

        try:
            return self.terms[term]
        except KeyError as e:
            if term not in self.missingTermDict:
                print("Failed to get term： {}".format(term))
                print("Try to get synonym term")
                checkSeries = self.terms.apply(lambda dagTerm: term in dagTerm.synonym)
                if checkSeries.sum() == 0:
                    raise KeyError("No similar term found for: {}".format(term))
                elif checkSeries.sum() > 1:
                    raise KeyError("No similar term found for: {}".format(
                        ", ".format(list(checkSeries[checkSeries].index)))
                    )
                else:
                    synTerm = list(checkSeries[checkSeries].index)[0]
                    print("{} is similar term with {}".format(synTerm, term))
                    self.missingTermDict[term] = synTerm
                    return self.getTerm(synTerm)
            else:
                return self.getTerm(self.missingTermDict[term])

    def getTerms(self, index):
        if isinstance(index, pd.Series):
            index = index.to_list()

        try:
            return [self.getTerm(term) for term in index]
        except KeyError:
            raise ExistsError("{}({}) should be passed as index".format(self.termsIndexName, index))

    def sortTerms(self, terms):
        def searchChildren(root, sortedTerm):
            if root.children and len(sortedTerm) != len(terms):
                for child in root.children:
                    if child in terms and child not in sortedTerm:
                        sortedTerm.append(child)
                    sortedTerm = searchChildren(child, sortedTerm)
            return sortedTerm

        terms = self.getTerms(terms)
        return searchChildren(self.root, sortedTerm=[])
    # def returnTermsId(self):
    #     return self.terms.apply(lambda x: x.ID).to_list()
    #
    # def returnTermsName(self):
    #     return self.terms.apply(lambda x: x.Name).to_list()

    def __get_sub(self, newRoot):
        termSeries = self.terms.loc[self.terms.apply(lambda x: x.isDescendant(newRoot))]
        return DAG(newRoot, termSeries, termsIndexName=self.termsIndexName, get_sub=True)

    @staticmethod
    def __modifyTermForSub(newRoot, term):
        term.depth = 0
        newParents = []
        for parent in term.parents:
            if parent.isDescendant(newRoot):
                newParents.append(parent)
        term.parents = newParents
        term.parentsIds = [parent.id for parent in term.parents]
        return term

    def getSub(self, newRoot):
        if isinstance(newRoot, str):
            newRoot = self.getTerm(newRoot)
        termSeries = (self.terms.loc[self.terms.apply(lambda x: x.isDescendant(newRoot))]).copy()
        termSeries = termSeries.apply(lambda term: self.__modifyTermForSub(newRoot, term))
        return DAG(newRoot, termSeries, termsIndexName=self.termsIndexName)
    
    def simplyTerms(self, termList, delTerms=[]):
        if delTerms:
            termList = list(set(termList)-set(delTerms))

        termList = np.array(self.getTerms(termList))  # actually, it's an array
        termArray = np.array(
            list(map(
                lambda x: list(map(
                    lambda y: x.isDescendant(y), termList
                )), termList
            ))
        )
        termResults = termList[termArray.sum(axis=1) == 1]

        transDict = {}
        for ancestor in termResults:
            ancestorName = ancestor.name
            for descendant in termList:
                if descendant.isDescendant(ancestor):
                    if transDict.get(ancestorName, False):
                        transDict[ancestorName].append(descendant.name)
                    else:
                        transDict[ancestorName] = [descendant.name]
        return termResults, transDict

    def returnIsInDf(self, ancestors, descendants):
        ancestors = [
            ancestor if isinstance(ancestor, DAGTerm) else self.getTerm(ancestor) for ancestor in ancestors
        ]
        descendants = [
            descendant if isinstance(descendant, DAGTerm) else self.getTerm(descendant) for descendant in descendants
        ]

        import pandas as pd

        isInData = []
        for ancestor in ancestors:
            isInData.append(list(map(lambda descendant: descendant.isDescendant(ancestor), descendants)))

        isInDf = pd.DataFrame(
            isInData,
            index=[ancestor.name for ancestor in ancestors],
            columns=[descendant.name for descendant in descendants]
        )
        return isInDf

    # def returnAdjMatrix(self):
    #     adjMatrix =

    def returnTermsWithSameDepth(self, depth, root=False):
        dag = self if not root else self.__get_sub(root)
        depth = depth if not root else root.depth + depth
        terms = dag.terms.apply(lambda x: x if x.depth == depth else np.nan)
        return terms.dropna()

    def returnLeafNode(self, root=False):
        dag = self if not root else self.__get_sub(root)
        return dag.terms[dag.terms.apply(lambda x: x.children==[])]

    def returnNetworkWithDepth(self, depth, root=False):
        G = nx.DiGraph()
        dag = self if not root else self.__get_sub(root)
        baseDepth = 0 if not root else root.depth
        if depth > dag.level:
            raise ExistsError("Depth should not be larger than {}".format(DAG.level))
        for i in range(baseDepth, baseDepth + depth):
            nodes = dag.returnTermsWithSameDepth(depth=i).to_list()
            nodesList = [(node.name, {"depth": i, "id": node.id}) for node in nodes]
            G.add_nodes_from(nodesList)
            for node in nodes:
                edgesList = [(node.name, child.name) for child in node.children if child.depth < baseDepth + depth]
                G.add_edges_from(edgesList)
        return G

    @classmethod
    def __getCountForTerm(cls, rootTerm, baseDict, resultDict, method):
        if rootTerm.name in resultDict:
            return [resultDict[rootTerm.name], None]
        baseCount = 0 if rootTerm.name not in baseDict else baseDict[rootTerm.name]
        if not rootTerm.children:
            resultDict[rootTerm.name] = baseCount
            return [baseCount, resultDict]
        for child in rootTerm.children:
            divideNum = 1 if method == "notDivide" else len(child.parents)
            childCount = cls.__getCountForTerm(child, baseDict, resultDict, method)[0] / divideNum
            baseCount += childCount
        resultDict[rootTerm.name] = baseCount
        return [baseCount, resultDict]

    @classmethod
    def __fillDict(cls, rootTerm, baseDict, method):
        resultDict = cls.__getCountForTerm(rootTerm, baseDict=baseDict, resultDict={}, method=method)[1]
        return resultDict

    def returnCountDict(self, initDict, method):
        if method not in ["notDivide", "divide"]:
            raise ExistsError("method should be set as 'notDivede' or 'divide'!!!")
        return self.__fillDict(self.root, baseDict=initDict, method=method)


if __name__ == "__main__":
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
        relationShipDict={"childrenIds": termSeries["childIds"].split("\n") if termSeries["childIds"] is not nan else []}
    ))
    DAGDf["term"].apply(lambda term: term.setTermFromDf(termDf=DAGDf, idColName="id", termsColName="term"))
    dagDAG = DAG(DAGDf.loc[0, "term"], DAGDf["term"], termsIndexName="name")

    # term_1 = dagDAG.getTerm("1")
    # childTerms = term_1.getTermsByChildDepth(childDepth=2)
    # dagDAG.simplyTerms(childTerms)
    #
    # isInDf = dagDAG.returnIsInDf(ancestors=["1", "2"], descendants=["4", "5", "6"])
    # print("Test has been done successfully")


