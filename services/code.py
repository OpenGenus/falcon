import json
import argparse
import os
import sys
import webbrowser
from . import getSearchResults
from . import recommendationUtils
import pathlib


ROOT_PATH = pathlib.Path(__file__).parents[1].as_posix()
category = json.load(open(ROOT_PATH+"/dumps/category.json", "r"))


def get_code(term, language, control):
    # converts filesystem to a nested dict
    dict_add = lambda x, y={}: dict_add(x[:-1], y).setdefault(x[-1], {}) if (x) else y
    baseDict = {}
    list(
        map(
            lambda x: dict_add(x, baseDict),
            [path["location"].split("/") for path in category],
        )
    )

    searchResults = getSearchResults.getSearchResults(term)
    print(searchResults)
    term = searchResults[0]["location"].split("/")[-1]

    allPaths = []
    childPath = []
    recommendationUtils.getPath(term, baseDict, "", allPaths, childPath)
    print(allPaths)
    print(childPath)
    if not len(childPath[0]):
        path = searchResults[0]["location"]
        path = "cosmos" + path
        if not os.path.exists(path):
            print("Clone the cosmos repo first into root of project")
            sys.exit()
        print(path)
        arr = os.listdir(path)
        print(arr)
        if not language:
            print("Available options")
            for code in arr:
                print(code.split(".")[-1])
            path = path + "/" + arr[0]
            print(path)
            if control == "open":
                webbrowser.open(path)
            else:
                sys.exit()

        else:
            for code in arr:
                if code.split(".")[-1] == language:
                    print(code)
    else:
        print("similar categories")
        for results in searchResults:
            print(results["category"])


def main(*args):
    if len(args) == 0:
        parser = argparse.ArgumentParser()
        parser.add_argument("--term", help="The term to look for")
        parser.add_argument(
            "--language", default="cpp", help="enter the language extension"
        )
        parser.add_argument(
            "--control",
            help="enter what to do with end file can be save,edit or delete",
        )
        args = parser.parse_args()
        term = args.term
        language = args.language
        control = args.control
    else:
        term = args[0]
        language = args[1]
        control = args[2]

    if not term:
        print("Enter a valid term")
        sys.exit()

    get_code(term, language, control)


if __name__ == "__main__":
    main()
