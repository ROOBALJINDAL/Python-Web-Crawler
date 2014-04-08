import sys
#words=input("ENTER NO OF WORDS: ")
s=input("ENTER SPACE ENTERED: ")
m=input("ENTER CONCANATED STRING: ")
flag=i=status=words=0
for i in range(len(s)):
  if s[i] == ' ':
    words+=1
words+=1
print words
s=s.replace(' ','')
length=len(s)/words
dd=i=minloc=0
copy=s

while status!=1:
  minloc=loc=min=k=i=flag=0
  j=length
  copy=s 

  for k in range(words):
    if k==0:
      minloc=loc=m.find(copy[i:j])
    else:
      loc=m.find(copy[i:j])
    if minloc== -1 or loc== -1:
      print 'STRING NOT FOUND'
      sys.exit()
    i+=length
    j+=length
    if loc<minloc:
      minloc=loc
  min=minloc

  for k in range(words):
    loc= copy.find(m[min:min+length])
    if loc != -1:
      flag+=1
      copy=copy.replace(copy[loc:loc+length],"",1)
      
    else:
      m=m.replace(m[0:minloc+length],"",1)
      break    

    min+=length

  if flag==words:
    print 'STRING FOUND'
    status=1
    i=input()
    sys.exit()
