import getSearchResults
import recommendationUtils
import json

term = "linear"

category = json.load( open( "dumps/category.json", "r" ) )


#converts filesystem to a nested dict
dict_add = lambda x, y={}: dict_add(x[:-1], y).setdefault(x[-1], {}) if(x) else y
baseDict = {}
map(lambda x: dict_add(x, baseDict), [path['location'].split("/") for path in category])


searchResults = getSearchResults.getSearchResults(term)
print searchResults
term = searchResults[0]['location'].split('/')[-1]

allPaths = []
childPath=[]
recommendationUtils.getPath(term,baseDict,'',allPaths,childPath)
print allPaths
print childPath
if not len(childPath[0]):
    print "end category"

