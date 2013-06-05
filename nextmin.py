num1=2241
num2=124

def convert2int(lst):
  s=map(str,lst)
  return int(''.join(s)) 

def compare(num, result,l,digits):
  s1=str(num)[:l+1]
  n1=convert2int(s1)
  n2=convert2int(result[:l+1])
  if l==(digits-1):
    return n2>n1
  return n2>=n1
  

def find_next(x,num,result,digits,l):
  if l==digits:
    print 'found:'+''.join(map(str,result))
    return
  for i in xrange(10):
    if i in x:
      result[l]=i
      if compare(num,result,l,digits):
        find_next(x,num,result,digits,l+1)

s1=str(num1)
s2=str(num2)
x=set([])
for c in str(num1): x.add(int(c))
digits=len(s2)
result=[0]*5
find_next(x,num2,result,digits,0)
