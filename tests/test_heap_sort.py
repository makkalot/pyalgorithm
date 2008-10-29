from pyalgorithm.util import *
from pyalgorithm.py_heap_sort import heap_sort

def test_heap_sort():
    from copy import copy
    how_many = 100000
    max_range = 100000
    how_many_test = 100

    for x in xrange(how_many_test):
        
        main_array = generate_int(1,max_range,how_many)
        copy_array = copy(main_array)
        copy_array.sort()
        heap_sort(main_array)
        assert main_array == copy_array
        
        if x%10==0:
            print "%d Test completed for heap "%x


