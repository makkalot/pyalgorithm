#A Python implementation of Quick Sort Algorithm

def qsort1(array):
    """
    First implementation of qsort will have more optimized
    ones later in that file :) That version has O(n) more space
    """

    if len(array)<=1:
        return array

    less = []
    greater = []

    pivot_index = len(array)/2
    pivot = array[pivot_index]
    #remove that from there
    array.remove(array[pivot_index])

    for i in array:
        if pivot>=i:
            less.append(i)
        else:
            greater.append(i)

    print "Pivot is : ",pivot
    print "Less is ",less
    print "Greater is ",greater

    return qsort1(less) +[pivot] + qsort1(greater)


if __name__ == "__main__":
    main_array = [2,8,7,1,3,5,6,4]
    #print partition_array(main_array,0,len(main_array)-1)
    #print main_array
    print qsort1(main_array)
    #print main_array
