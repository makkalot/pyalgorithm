from pyalgorithm.my_merge import *
from pyalgorithm.util import *

def test_merge_part():
    from copy import copy
    how_many = 100
    max_range = 10000
    
    for x in xrange(10):
        for left_many in xrange(1,how_many):
            for right_many in xrange(1,how_many):
                
                left_array = generate_int(1,max_range,left_many)
                right_array = generate_int(1,max_range,right_many)
        
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
            
                main_array = merge_action(left_array,right_array)
                #print main_array
                #print copy_main
                assert copy_main == main_array
                
        print "%d Test completed for merge "%x

def test_merge_sort():
    
    from copy import copy
    how_many = 1000
    max_range = 10000
    
    for x in xrange(100):
        main_array = generate_int(1,max_range,how_many)
        copy_main = copy(main_array)
        copy_main.sort()

        main_array = merge_sort(main_array)
        assert copy_main == main_array
    
        if x%10 == 0:
            print "%d Test completed for merge "%x
