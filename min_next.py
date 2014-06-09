from collections import defaultdict

num1=2241
num2=123

def convert2int(lst):
  return int(''.join(map(str,lst))) 

def compare(num, result,l,digits):
  n1=convert2int(str(num)[:l+1])
  n2=convert2int(result[:l+1])
  if l==(digits-1):
    return n2>n1
  return n2>=n1
  

def find_next(x1,num,result,digits,l):
  if l==digits:
    print 'found:'+''.join(map(str,result))
    return
  for i in xrange(10):
    x=x1.copy()
    if x[i]>0:
      result[l]=i
      x[i]-=1
      if compare(num,result,l,digits):
        find_next(x,num,result,digits,l+1)

s1=str(num1)
s2=str(num2)
x=defaultdict(int)
for c in str(num1): x[int(c)]+=1
digits=len(s2)
result=[0]*5
find_next(x,num2,result,digits,0)
