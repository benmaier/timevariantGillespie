from dynamicGillespie import dynamicGillespie
import cPickle as pickle
import networkx as nx
from numpy import logspace
import sys

R0 = float(sys.argv[1])

beta=1.
#alpha=

gil = dynamicGillespie(verbose=True)  #initialise
gil.init_from_file('conference_dtu.csv')   #read in links from file
gil.duration = 14   # set the duration of the simulation (in days)
gil.set_disease_params( { 'R0': R0,
                          'beta':beta,
                        })
gil.simulate('original', int(gil.N*0.1), loop = 1) #run simulation 10 times (the loop argument)

path='./test/socio_test_R0_%4.2f.pickle' % R0
gil.save(path,mkdir = True) #save the results
