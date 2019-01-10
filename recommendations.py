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

def getMaxDepthofDict(d, level=1):
    if not isinstance(d, dict) or not d:
        return level
    return max(getMaxDepthofDict(d[k], level + 1) for k in d)
  
def getPath(element, JSON, path, all_paths):    
  if element in JSON:
    path =  path + element #+ str(JSON[element])
    global childPath
    childPath = JSON[element]
    # print(childPath)
    # print path
    all_paths.append(path)
  for key in JSON:
    if isinstance(JSON[key], dict):
      getPath(element, JSON[key],path + key + '/',all_paths)

def getParentWeightedList(l):
  maxDepth = getMaxDepth(l)
  parentWeights =  []
  for i in range(0,maxDepth):
    parentWeights.append([])
  for data in l:
    i=0
    for  path in data.split("/"):
      parentWeights[i].append(path)
      i=i+1
  return parentWeights

def getChildWeights():
  maxDepth = getMaxDepthofDict(childPath)
  print maxDepth
  childWeights =  []
  for i in range(0,maxDepth):
    childWeights.append([])
  
  for r, s in childPath.items():
    i=0
    q = []
    p = r
    while True:
        for k, v in s.items():
            # print('(%s,%s) ' % ('ROOT' if p == r else p, k))
            # if k != "test" and k != "src":
            #     print k.replace('_',' ')
            childWeights[i].append(k)
            if v:
                q.append((k, v))
        if not q:
                break
        p, s = q.pop(0)
  print childWeights

# print(baseDict)
all_paths = []

getPath('artificial_intelligence',baseDict,'',all_paths)
print(all_paths)
print(getMaxDepth(all_paths))
print(getParentWeightedList(all_paths))
# print childPath
getChildWeights()