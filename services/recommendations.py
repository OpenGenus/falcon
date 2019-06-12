import json
import argparse
import sys
from . import getSearchResults
from . import recommendationUtils
import pathlib

ROOT_PATH = pathlib.Path(__file__).parents[1].as_posix()
category = json.load(open(ROOT_PATH+"/dumps/category.json", "r"))


def get_recommendation(searchResults, recTerm, top, types):
    recTerm = searchResults[0]["location"].split("/")[-1]
    # print recTerm
    # converts filesystem to a nested dict
    dict_add = lambda x, y={}: dict_add(x[:-1], y).setdefault(x[-1], {}) if (x) else y
    baseDict = {}
    list(
        map(
            lambda x: dict_add(x, baseDict),
            [path["location"].split("/") for path in category],
        )
    )

    allPaths = []
    childPath = []
    recommendationUtils.getPath(recTerm, baseDict, "", allPaths, childPath)
    if len(childPath) > 0:
        childPath = childPath[0]
    # print(allPaths)
    # print(getMaxDepth(allPaths))
    recDict = []

    print("childPath")
    print(childPath)
    if types != "child":
        print("parent")
        parentWeights = recommendationUtils.getParentWeightedList(allPaths)
        maxParentWeight = len(parentWeights)
        for parents in parentWeights:
            for parent in parents:
                recDict.append({parent: maxParentWeight})
            maxParentWeight = maxParentWeight - 1

    # print childPath
    if types != "parent":
        childWeights = recommendationUtils.getChildWeightedList(childPath)
        maxChildWeight = len(childWeights) + 1

        for childs in childWeights:
            for child in childs:
                recDict.append({child: maxChildWeight})
            maxChildWeight = maxChildWeight - 1
    # print childWeights

    finalRecDict = sorted(recDict, key=lambda x: list(x.values()), reverse=True)
    if top:
        for i in range(0, int(top)):
            print((finalRecDict[i]))
    else:
        for data in finalRecDict:
            print(data)


def main(*args):
    if len(args) == 0:
        parser = argparse.ArgumentParser()
        parser.add_argument("--recommend", help="The recommendation term")
        parser.add_argument("--top", help="Number of results to show")
        parser.add_argument(
            "--type", help="type of recommendation can be parent/child/all"
        )
        args = parser.parse_args()
        recTerm = args.recommend
        top = args.top
        types = args.type
    else:
        recTerm = args[0]
        top = args[1]
        types = args[2]

    if recTerm == None:
        print("please enter a term to get recommendation")
        sys.exit()

    if types != "parent" and types != "all" and types != "child":
        print("please enter correct type which can be child/parent/all")
        sys.exit()

    searchResults = getSearchResults.getSearchResults(recTerm, None)

    if len(searchResults) == 0:
        print("Nothing to recommend")
        sys.exit()

    get_recommendation(searchResults, recTerm, top, types)


if __name__ == "__main__":
    main()
