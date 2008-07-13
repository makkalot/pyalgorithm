from abstract import AbstractAlgorithm

class MergeSort(AbstractAlgorithm):
    name = ""
    o_notation = ""

    def implement(self,array,start,stop):
        """
        Merge sort implementation a
        recursive one :)
        """
        if start < stop:
            splitter = (start+stop)/2
            self.implement(array,start,splitter)
            self.implement(array,(splitter+1),stop)
            self.merge(array,start,splitter,stop)


    def merge(self,array,start,splitter,stop):
        """
        Merges two parts of an array into itself ...
        """
        #split the array into a left and a right partition
        left_array = array[start:splitter]
        right_array = array[splitter:stop]
        #print "The inner left :",left_array 
        #print "The inner right :",right_array 
        
        l_i=0
        r_i=0
        early_exit = None

        #do the merging here
        for main_index in xrange(start,stop):
            if left_array[l_i] < right_array[r_i]:
                array[main_index]=left_array[l_i]
                l_i += 1
                if l_i == splitter:
                    early_exit='left'
                    break
            else:
                array[main_index]=right_array[r_i]
                r_i +=1
                if r_i == (stop-splitter):
                    early_exit='right'
                    break
        #print "The inner main :",array


        if early_exit:
            if early_exit=='left':
                array[(l_i+r_i):stop] = right_array[r_i:len(right_array)]
            elif early_exit=='right':
                array[(l_i+r_i):stop] = left_array[l_i:len(left_array)]
        
        #print array
                

if __name__ == "__main__":
    pass


