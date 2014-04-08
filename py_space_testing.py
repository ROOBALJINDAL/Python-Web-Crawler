import sys
words=3
#s='a e i o u'
#m='kkdjfkggioemeloeoidkoiueanf'
s='roobal jindal deepak'
m='jindalsjhddeepakjindalskhdndeepakjindalroobalmdj'
s=s.replace(' ','')
length=len(s)/words
dd=i=minloc=0
flag=status=0
copy=s

while status!=1:
  minloc=loc=min=k=i=flag=0
  j=length
  #print "STARTING: "
  #dd=raw_input()
  copy=s 
  
  #print "COPY: " + copy
  #print "M: " + m 
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
  #print m[minloc:minloc+length]
  #print minloc
  #dd=raw_input()

  for k in range(words):
    loc= copy.find(m[min:min+length])
    if loc != -1:
      flag+=1
      #print 'copy= ' + copy 
      #print "removed from COPY: " + copy[loc:loc+length]      
      copy=copy.replace(copy[loc:loc+length],"",1)
      
    else:
      #print minloc
      #print "removed from m: " + m[minloc:minloc+length]
      m=m.replace(m[0:minloc+length],"",1)
      #print 'm= ' + m
      #print 'BREAK'
      #dd=raw_input()
      break
     
    
    min+=length
    #dd=raw_input()

  if flag==words:
    print 'STRING FOUND'
    status=1
  

z=input()
