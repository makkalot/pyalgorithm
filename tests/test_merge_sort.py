from pyalgorithm.merge_sort import MergeSort
from pyalgorithm.util import *

def test_merge_part():
    from copy import copy
    how_many = 100
    max_range = 100000
    
    for x in xrange(10):
        for splitter in xrange(1,(how_many*2)):
            
            left_array = generate_int(1,max_range,splitter)
            right_array = generate_int(1,max_range,(how_many*2)-splitter)
            
            #sort both and merge into a one
            left_array.sort()
            right_array.sort()
            #print "\n\nThe left array is :",left_array
            #print "The right array is :",right_array
            
            main_array = left_array + right_array
            copy_main = copy(main_array)
            #print "The copy main is :",copy_main
            copy_main.sort()
            #print "The copy main is :",copy_main
            
            merger = MergeSort()
            merger.merge(main_array,0,splitter,(how_many*2))
            #print "The main array is :",main_array 
            assert copy_main == main_array
            
        if x%10==0:
            print "%d Test completed for merge "%x

def test_merge_sort():
    from copy import copy 
    max_range = 100
    how_many = 10

    for x in xrange(1):

        m = MergeSort()
        main_array = generate_int(1,max_range,how_many)
        copy_array = copy(main_array)
        copy_array.sort()
        m.implement(main_array,0,len(main_array))

        assert copy_array == main_array


