import json
import argparse
import sys
import getSearchResults

category = json.load( open( "dumps/category.json", "r" ) )

parser = argparse.ArgumentParser()
parser.add_argument("--recommend", help='The recommendation term')
parser.add_argument("--top", help='Number of results to show')
parser.add_argument("--type", help='type of recommendation can be parent/child/all')

args = parser.parse_args()

recTerm = args.recommend
top = args.top
types = args.type
if(types !="parent" and  types !="all" and types !="child" ):
  print "please enter correct type which can be child/parent/all"
  sys.exit()


# print recTerm


if recTerm == None:
  print("please enter a term to get recommendation")
  sys.exit()

searchResults = getSearchResults.getSearchResults(recTerm,None)

if len(searchResults)==0:
  print("Nothing to recommend")
  sys.exit()

recTerm = searchResults[0]['location'].split('/')[-1]
# print recTerm
#converts filesystem to a nested dict
dict_add = lambda x, y={}: dict_add(x[:-1], y).setdefault(x[-1], {}) if(x) else y
baseDict = {}
map(lambda x: dict_add(x, baseDict), [path['location'].split("/") for path in category])

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


allPaths = []
childPath=[]
getPath(recTerm,baseDict,'',allPaths,childPath)
if len(childPath)>0:
  childPath = childPath[0]
# print(allPaths)
# print(getMaxDepth(allPaths))
recDict = []

if types != "child":
  print "parent"
  parentWeights = getParentWeightedList(allPaths)
  maxParentWeight = len(parentWeights)
  for parents in parentWeights:
    for parent in parents:
      recDict.append({parent:maxParentWeight})
    maxParentWeight = maxParentWeight -1

# print childPath
if types != "parent":  
  childWeights = getChildWeightedList(childPath)
  maxChildWeight = len(childWeights) + 1

  for childs in childWeights:
    for child in childs:
      recDict.append({child:maxChildWeight})
    maxChildWeight = maxChildWeight -1
# print childWeights



finalRecDict = sorted(recDict, key=lambda x: x.values(),reverse=True)
if top:
  for i in range(0,int(top)):
    print(finalRecDict[i])
else:
  for data in finalRecDict:
    print data
