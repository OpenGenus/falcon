import pygtrie
import json
import pickle

category = json.load( open( "dumps/category.json", "r" ) )
trie = pygtrie.CharTrie()
catMap = dict()
idx = int(0)
for data in category:
    description = data["description"]
    trie[description] =  True
    catMap[description] = idx
    idx= idx +1

pickle.dump( trie, open( "dumps/trie.p", "wb" ))
pickle.dump( catMap, open( "dumps/catMap.json","w"))
# to load back
# u = pickle.load( open( "trie.p", "rb" ) )  to load back
# u = pickle.load( open( "dumps/catMap.json", "r" ) )