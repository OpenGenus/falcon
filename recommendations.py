import json
category = json.load( open( "dumps/category.json", "r" ) )

#converts filesystem to a nested dict
dict_add = lambda x, y={}: dict_add(x[:-1], y).setdefault(x[-1], {}) if(x) else y
baseDict = {}
map(lambda x: dict_add(x, baseDict), [path['location'].split("/") for path in category])

# #seaches for the required key
# def findkeys(node, kv):
#     if isinstance(node, list):
#         for i in node:
#             for x in findkeys(i, kv):
#                yield x
#     elif isinstance(node, dict):
#         if kv in node:
#             yield node[kv]
#         for j in node.values():
#             for x in findkeys(j, kv):
#                 yield x

# results= list(findkeys(baseDict, 'artificial_intelligence'))
# print baseDict
# print(results)
# d = {"results":results[0]}
# #does a bfs for the formed dictionary
# for r, s in d.items():
#     q = []
#     p = r
#     while True:
#         for k, v in s.items():
#             print('(%s,%s) ' % ('ROOT' if p == r else p, k))
#             # if k != "test" and k != "src":
#             #     print k.replace('_',' ')
#             if v:
#                 q.append((k, v))
#         if not q:
#                 break
#         p, s = q.pop(0)

def getMaxDepth(l):
  maxDepth = 1
  for data in l:
    maxDepth = max(maxDepth,len(data.split("/")))
  return maxDepth

def getWeightedList(l):
  maxDepth = getMaxDepth(l)
  weights =  []
  for data in l:
    if(maxDepth == len(data.split("/"))):
      i=0
      for words in data.split("/"):
        weights.append({words:i})
        i=i+1
      return weights
  return weights
      
def getPath(element, JSON, path, all_paths):    
  if element in JSON:
    path =  path + element #+ str(JSON[element])
    print path
    all_paths.append(path)
  for key in JSON:
    if isinstance(JSON[key], dict):
      getPath(element, JSON[key],path + key + '/',all_paths)

# print(baseDict)
all_paths = []
getPath('perceptron',baseDict,'',all_paths)
print(all_paths)
print(getMaxDepth(all_paths))
print(getWeightedList(all_paths))