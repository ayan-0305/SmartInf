import pickle
import networkx as nx
from operator import itemgetter
from random import randint
from datetime import datetime
startTime = datetime.now()
import matplotlib.pyplot as plt
#import seaborn as sns
#import pandas as pd
import pylab as pl
import numpy as np


# Constructing final ranked influencer list after refinement of ranking given by SmartInf-Temp

def n_u(G, node):
	return list(G.neighbors(node))+[node] 

def check_redundancy(List1, List2):
	S1 = set(List1)
	for k in List2:
		try:
			List1.remove(k)
		except:
			pass
	S2 = set(List1)
	if(S1==S2):
		return True
	else:
		return False

Temporal=[]
f=open("ranked-list-T.txt",'r')
for line in f:
	t=line.split()
	Temporal.append(t[0])
	
G = nx.DiGraph()
followers = pickle.load( open( "sample-follower-network.p", "rb" ) )
for key in followers.keys():
	for node in followers[key]:
		G.add_edge(key, node)

print "Nodes in G:", len(G.nodes())

ind=0
Exposed=[]
S=[]

while(ind<len(Temporal) and len(Exposed)<len(G.nodes())):
	if( len(set(n_u(G,Temporal[ind])).difference(Exposed)) > 1):
		S.append(Temporal[ind])
		Exposed = list(set(Exposed) | set(n_u(G, Temporal[ind])))

	ind+=1
	
print "Total nodes: ", G.number_of_nodes()
print "size of Ranked list of influencers (before refinement): ", len(Temporal)
print "size of Final Ranked list of influencers (after refinement): ", len(S)



f=open("final-ranked-list-after-refinement-S.txt",'w')
for i in range(0,len(S)):
    f.write(str(S[i]))
    f.write('\n')
	

print "Time Taken: ", datetime.now() - startTime,"h:m:s.ms"



