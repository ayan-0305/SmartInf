import numpy as np
import math
import pickle
from datetime import datetime
startTime=datetime.now()


#Detection of first peak indices of type I cascades

f=open("sample-time-intervals.txt",'r')
typeI={}
for line in f:
	t=line.split()
	l=[]
	if len(t)>=10:
		for i in range(1,len(t)):
			l.append(float(t[i]))
		m=np.mean(l)
		n=math.sqrt(np.var(l))
		for i in range(0,len(l)):
			if l[i]>m+2*n:
				if 0.2*len(l)<=i and i<=0.8*len(l):
					typeI[t[0]]=i
					break

pickle.dump(typeI,open("typeI-peakInd.p","wb"))


#Computation of fall index after first peak of type I cascades

f=open("sample-time-intervals.txt",'r')
falls={}
for line in f:
	t=line.split()
	if t[0] in typeI.keys():
		p=typeI[t[0]]
		l=[]
		for i in range(1,len(t)):
			l.append(float(t[i]))
		m=np.mean(l)
		n=math.sqrt(np.var(l))
		for i in range(p+1,len(l)):
			if l[i]<=m+2*n:
				falls[t[0]]=i
				break

pickle.dump(falls,open("typeI-fallInd.p","wb"))


print datetime.now()-startTime



