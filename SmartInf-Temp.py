import numpy as np
import math
import pickle
from datetime import datetime
startTime=datetime.now()




#Identification of potential influencers for all Type I cascades

f=open("sample-cascade-sorted-user-sequence.txt",'r')
d=pickle.load(open("typeI-peakInd.p","rb"))
d1=pickle.load(open("typeI-fallInd.p","rb"))
act_period={}
potential_inf={}
for line in f:
	t=line.split()
	if t[0] in d.keys() and t[0] in d1.keys():
		l=[]
		potential_inf[t[0]]=[]
		for i in range(1,len(t)):
			l.append(t[i])
		delta=d1[t[0]]-d[t[0]]
		act_period[t[0]]=delta
		for i in range(d[t[0]],d1[t[0]]+1):
			potential_inf[t[0]].append(l[i])

global_potential_inf=[]
for k in potential_inf.keys():
	global_potential_inf=list(set(global_potential_inf) | set(potential_inf[k]))



# Ranking of global set of potential influencers across all Type I cascades

f=open("sample-cascade-sorted-user-sequence.txt",'r')
freq={}
for x in global_potential_inf:
	freq[x]=0
for line in f:
	t=line.split()
	if t[0] in act_period.keys():
		l=[]
		for i in range(1,len(t)):
			l.append(t[i])
		for i in range(d[t[0]],d1[t[0]]+1):
			if l[i] in global_potential_inf:
				freq[l[i]]+=1


f=open("ranked-list-T.txt",'w')
for key, value in sorted(freq.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    f.write(str(key))
    f.write(' ')
    f.write(str(value))
    f.write('\n')



print datetime.now()-startTime