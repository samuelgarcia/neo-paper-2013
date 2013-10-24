import numpy as np
import quantities as pq


n = 1000000000
filename = 'test_big'

def create():
    f = open(filename, 'w')
    a = np.zeros(n, dtype = float)
    f.write(a)
    f.close()


def np_memmap_read():
    a = np.memmap(filename, dtype = float)
    #This is instantaneous
    print a[n/2]


def pq_memmap_read():
    a = np.memmap(filename, dtype = float)
    #This is instantaneous
    b = pq.Quantity(a, units=pq.s, copy = False )
    print b[n/2]

    #This is read the file entirely
    #~ b = pq.Quantity(a, units=pq.s, copy = True )
    #~ print b[n/2]

    


#~ create()
np_memmap_read()
pq_memmap_read()
