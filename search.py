import pickle
import collections
import json

trie = pickle.load( open( "dumps/trie.p", "rb" ) )  
catMap = pickle.load( open( "dumps/catMap.p", "rb" ) )
category = json.load( open( "dumps/category.json", "r" ) )


searchTerm = "greedy algorithms"
searchTerms = searchTerm.split()
results = []
for terms in searchTerms:
    if trie.get(terms):
        for value in catMap[terms]:
            results.append(value)

counts = collections.Counter(results)
results = sorted(results, key=lambda x: -counts[x])
searchResults = []
[searchResults.append(x) for x in results if x not in searchResults]

print searchResults
for data in searchResults:
    print category[data]['description']
