'''
 K-Way merging of a number of sorted files
 Each file object has a custom __cmp__ function
 All file handles go to a PriorityQueue
 Iterate throug the queue and read lines
 If after reading file handle is still valid, put it back to queue
 
'''
import sys
from Queue import PriorityQueue
import heapq

fps=[]
n=50

for i in xrange(n):
  fps.append(open('agg_%02d_sort1.txt'%i,'r'))

class FP: 
  def __init__(self, fp, id):
    self.fp = fp
    self.id = id
    self.readline()

  def getid(self):
    return self.id

  def getline(self):
    return self.line

  def readline(self):
    self.line = self.fp.readline().strip()
    if self.line:
      self.q,self.u,self.w = self.line.split('\t')
      self.w = int(self.w)

  def __cmp__(self, other):
    return cmp(self.getkey(), other.getkey())

  def getkey(self):
    return self.q+'\t'+self.u

  def getw(self):
    return self.w

  def __str__(self):
    return self.q+'\t'+self.u+'\t'+str(self.w) 

pq = PriorityQueue()
for i in xrange(n):
  pq.put(FP(fps[i], i))

ckey=''#current key
cw=0
while(not pq.empty()):
  fp = pq.get()
  key = fp.getkey()
  if key==ckey:
    cw+=fp.getw()
  else:
   if ckey!='':
     print ckey+'\t'+str(cw)
   ckey = key
   cw = fp.getw()
  fp.readline()
  if fp.getline():
    pq.put(fp)

print ckey+'\t'+str(cw)

for i in xrange(n):
  fps[i].close() 
