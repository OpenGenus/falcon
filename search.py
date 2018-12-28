import pickle
import collections
import json
import sys

trie = pickle.load( open( "dumps/trie.p", "rb" ) )  
catMap = pickle.load( open( "dumps/catMap.p", "rb" ) )
category = json.load( open( "dumps/category.json", "r" ) )


searchTerm = " ".join(sys.argv[1:])
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

for data in searchResults:
    print category[data]['description']

if len(searchResults)==0:
    print "No results found for search"
