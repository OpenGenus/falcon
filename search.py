import pickle
import collections
import json
import sys
import argparse

trie = pickle.load( open( "dumps/trie.p", "rb" ) )  
catMap = pickle.load( open( "dumps/catMap.p", "rb" ) )
category = json.load( open( "dumps/category.json", "r" ) )


parser = argparse.ArgumentParser()
parser.add_argument("--search", help='The search term')
parser.add_argument("--results", help='Required number of results')

args = parser.parse_args()

searchTerm = args.search
display = args.results

if searchTerm==None:
    print("Enter a valid Search Term")
    sys.exit()

searchTerms = searchTerm.split()
results = []
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
        print category[data]['description']
        idx = idx+1
        if idx>int(display):
            sys.exit()


for data in searchResults:
    print category[data]['description']

if len(searchResults)==0:
    print "No results found for search"
