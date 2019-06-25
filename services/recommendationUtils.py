def getMaxDepth(l):
  maxDepth = 1
  for data in l:
    maxDepth = max(maxDepth,len(data.split("/")))
  return maxDepth

def getMaxDepthofDict(d, level=1):
    if not isinstance(d, dict) or not d:
        return level
    return max(getMaxDepthofDict(d[k], level + 1) for k in d)
  
def getPath(element, JSON, path, allPaths,childPath):    
  if element in JSON:
    path =  path + element #+ str(JSON[element])
    # global childPath
    childPath.append(JSON[element])
    # print(childPath)
    # print path
    allPaths.append(path)
  for key in JSON:
    if isinstance(JSON[key], dict):
      getPath(element, JSON[key],path + key + '/',allPaths,childPath)

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

def getChildWeightedList(childPath):
  try:
    maxDepth = getMaxDepthofDict(childPath)
    # print maxDepth
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
    return childWeights
  except:
    return []
