def max_heapify(main_array,index,heap_size):
    """
    Simply goes recursive and swaps if childs are bigger than
    parent
    Here heap size is an important part of the skill because when
    it is len(main_array) the max_heapify thing goes until to the end
    of the tree but when we decrement it ,it doesnt go to the end
    and that is important because in heap sort we do sth like 
    swap[0]<-->swap[index] so if it goes to the end it will pop
    the index again to the top so that is not we want here ...
    """

    #set the indexes for children
    left = (index*2)+1
    right = (index * 2) + 2
    #print "The starting index is :",main_array[index]
    largest = index

    if left <= heap_size:
        if main_array[left] > main_array[index]:
            largest = left

    #here we also compare it wit the left if it was choosen in previous if
    if right <= heap_size:
        if main_array[right] > main_array[largest]:
            largest = right
    
    #yep if we have found a bigger one we should swap em
    if largest != index:
        tmp = main_array[largest]
        main_array[largest] = main_array[index]
        main_array[index] = tmp
        #the swapped value may violate the leafs so we should continue checking from it !
        #that is an important point of view ...
        max_heapify(main_array,largest,heap_size)

def build_max_heap(main_array):
    """
    Method call the previous method max_heapify and converts 
    the current array into a max-heap
    """
    #we start from len(main_array)/2-1 because it is the
    #place where you have latest parents interesting really :)
    #it is up to -1 because xrange goes to end+1 last ...
    start = len(main_array)/2-1
    heap_size = len(main_array)-1

    for leaf in xrange(start,-1,-1):
        max_heapify(main_array,leaf,heap_size)

def heap_sort(main_array):
    """
    Method firstly calls the build_max_heap to create a max-heap
    data structure ,the second step is to swap the main_array[0]
    with the latest (which is the index into the for) member. Why
    we swap it with main_array[0] because in a max-heap structure
    it is the biggest member so ...
    """
    build_max_heap(main_array)
    heap_size = len(main_array)-1
    #print main_array
    for heap_member in xrange((len(main_array)-1),0,-1):
        tmp = main_array[0]
        main_array[0] = main_array[heap_member]
        main_array[heap_member] = tmp
        #print main_array
        heap_size -=1
        max_heapify(main_array,0,heap_size)

if __name__ == "__main__":
    """
    main_array = [16,4,10,14,7,9,3,2,8,1]
    print main_array
    max_heapify(main_array,1)
    print main_array
    
    main_array = [4,1,3,2,16,9,10,14,8,7]
    build_max_heap(main_array)
    print "The latest heap array is "
    print main_array
    """
    main_array = [4,1,3,2,16,9,10,14,8,7]
    main_array = [16,4,10,14,7,9,3,2,8,1]
    heap_sort(main_array)
    print main_array

