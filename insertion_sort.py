from abstract import AbstractAlgorithm

class InsertionSort(AbstractAlgorithm):
    
    name = "Insertion sort"
    o_notation = "N*N"

    def implement(array):
        """
        Insertion sort is cool because all the stuff is done in
        place you dont for any other arrays and objects but it is
        slow for bigger data sets cause it is N*N indeed.
        """

        for j in xrange(1,len(array)):
            # the one to be compared with others
            key = array[j]
            i = j-1

            while i>=0 and array[i]>key:
                array[i+1]=array[i]
                i=i-1

            array[i+1]=key

    implement = staticmethod(implement)

if __name__ == "__main__":
    pass
