import numpy as np
import pylab as pl
import seaborn as sns
import cPickle as pickle

a = pickle.load(open('./test/results.pickle','rb'))
res = a[0]

t = res['timeline']
I = res['prevalence']
SI = res['ISlinks']

pl.plot(t,I)
pl.plot(t,SI,alpha=0.5)

pl.show()
