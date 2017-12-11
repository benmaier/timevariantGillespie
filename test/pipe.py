from dynamicGillespie import dynamicGillespie
import sys
import pickle
import networkx as nx
from numpy import logspace

R0=2
beta=1./10

gil = dynamicGillespie()
gil.init_from_file('droplet.csv') #change this one to your path
gil.duration = 90
gil.set_disease_params({'R0':R0,'beta':beta})
gil.simulate('original', int(gil.N*0.1), loop = 10)

path='/home/olga/sims/DTU/endemic_fraction/original/results/droplet/'+str(R0)+'_'+str(beta)+'.pickle'
gil.save(path,mkdir = True)
