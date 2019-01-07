import json
category = json.load( open( "dumps/category.json", "r" ) )

#converts filesystem to a nested dict
dict_add = lambda x, y={}: dict_add(x[:-1], y).setdefault(x[-1], {}) if(x) else y
base_dict = {}
map(lambda x: dict_add(x, base_dict), [path['location'].split("/") for path in category])

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

# results= list(findkeys(base_dict, 'artificial_intelligence'))
# print base_dict
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

def getPath(element, JSON, path, all_paths):    
  if element in JSON:
    path =  path + element #+ str(JSON[element])
    print path
    all_paths.append(path)
  for key in JSON:
    if isinstance(JSON[key], dict):
      getPath(element, JSON[key],path + key + '/',all_paths)

# print(base_dict)
all_paths = []
getPath('perceptron',base_dict,'',all_paths)
print(all_paths)