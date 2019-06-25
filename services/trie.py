import pygtrie
import json
import pickle

category = json.load( open( "dumps/category.json", "r" ) )
trie = pygtrie.CharTrie()
catMap = dict()
idx = int(0)
for data in category:
    description = data["description"]
    for word in description.split():
        word = word.lower()
        trie[word] =  True
        if catMap.has_key(word):
            catMap[word].append(idx)
        else:
            catMap[word] = []
            catMap[word].append(idx)
    idx= idx +1
pickle.dump( trie, open( "dumps/trie.p", "wb" ))
pickle.dump( catMap, open( "dumps/catMap.p","wb"))
# to load back
# u = pickle.load( open( "trie.p", "rb" ) )  to load back
# u = pickle.load( open( "dumps/catMap.json", "r" ) )