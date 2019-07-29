import pickle
import collections
import json
import sys
import argparse
import pathlib
import time

ROOT_PATH = pathlib.Path(__file__).parents[1].as_posix()
trie = pickle.load(open(  ROOT_PATH + "/dumps/trie.p", "rb"))
catMap = pickle.load(open(ROOT_PATH + "/dumps/catMap.p", "rb"))
category = json.load(open(ROOT_PATH + "/dumps/category.json", "r"))

def writeToJSONFile(path, fileName, data):
    filePathNameWithExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWithExt, 'w') as fp:
        json.dump(data, fp)

def getSearchResults(searchTerm, output, display=None):
    """
    part of search.py script, which implements
    functionality similar to grep -ir <term>
    """
    start = time.time()
    path = './services'
    fileName = 'search_output'
    searchTerms = searchTerm.split()
    results = []
    newResults = []
    jsonData = {}
    jsonData['searchTearm'] = searchTerm
    for terms in searchTerms:
        terms = terms.lower()
        if trie.get(terms):
            for value in catMap[terms]:
                results.append(value)

    counts = collections.Counter(results)
    results = sorted(results, key=lambda x: -counts[x])
    searchResults = []
    [searchResults.append(x) for x in results if x not in searchResults]

    idx = 1
    if display:
        for data in searchResults:
            #print (category[data]['description'])
            newResults.append(category[data]['description'])
            results.append(category[data])
            idx = idx+1
            if idx>int(display):
                print ("\n".join(newResults))
                jsonData['numResults'] = display
                jsonData['results'] = newResults
                end = time.time()
                jsonData['timeTaken'] = end - start
                if output == "json":
                    print("\n")
                    print("JSON Format Output : ")
                    print(jsonData)
                return newResults

    results = []
    newResults = []
    for data in searchResults:
        newResults.append(category[data]['description'])
        results.append(category[data])
        
    print ("\n".join(newResults))
    return newResults

    # if len(searchResults)==0:
    #     print "No results found for search"
