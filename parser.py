from bs4 import BeautifulSoup as bs
from collections import Counter

def getDups(html):
  soup = bs(html, 'html.parser').body # get only the body of the html
  children = soup.findChildren() # get all the nodes
  count = Counter(children) # count of nodes with same value
  countList = list(count) # keys of count dict
  res = [] 

  for i in countList:
    parents = i.findParents() # get all the parents of a node
    pop = False
    for p in parents: # check if the parent is also repeating in which case child is not needed
      if p != soup:
        if count[p] == count[i]:
          pop = True
          break
    if pop or count[i] == 1:
      count.pop(i)
  updatedCount = list(count) # updates nodes
  for i in updatedCount: # convert to an array of object as proper response
    res.append({'repCode': i.prettify(), 'count': count[i], 'componentName': str(i.name)})
  return res
