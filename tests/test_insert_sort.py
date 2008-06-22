from pyalgorithm.insertion_sort import InsertionSort
from pyalgorithm.util import *

def test_insertion_sort():

    #test it at least 100 times with 1000 elements 
    for t in range(0,1000):
        array_to_sort = generate_int(1,100000,10000)
        assert array_to_sort.sort() == InsertionSort.implement(array_to_sort)
        
        if t%10 == 0:
            print "The test %d is done"%(t)
    print "Happy testing"


