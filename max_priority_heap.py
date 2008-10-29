from py_heap_sort import heap_sort,build_max_heap,max_heapify

class MaxHeap(list):

    """
    The MaxHeap is a child of list we know but has 
    some beautiful heap operations here.You are free
    to use list operations they wont break the heap
    structure but,sometimes they wont be very efficient
    so be careful !

    When you think you messed up sth you can run the build_max_heap
    again and all will be fixed, but try not to do that it may not be 
    very efficient on big arrays believe me :)
    """

    def __init__(self,list_ob=None):
        build_max_heap(list_ob)
        super(MaxHeap,self).__init__(list_ob)
        self.heap_size = len(list_ob)

    def rebuild_max_heap(self):
        build_max_heap(self)

    def insert(self,index,object):
        #that one is not efficient better dont use it  use
        #the insert_to_heap method instead of that :)
        super(MaxHeap,self).insert(index,object)
        build_max_heap(self)

    def insert_to_heap(self,object):
        """
        Insert a new element into the list but
        it is important to popup it into the right place 
        """
        self.heap_size +=1
        super(MaxHeap,self).append(object)
        self.increase_key(self.heap_size-1,object,bigger=False)

    def get_maximum(self):
        return self.__getitem__(0)

    def extract_max(self):
        """
        The method gets the max of that heap 
        actually it removes it so :)
        """
        if self.heap_size < 1:
            raise Exception("The heap is empty sorry")
        
        maximum = self.__getitem__(0)
        super(MaxHeap,self).__setitem__(0,self.__getitem__(self.heap_size-1))
        #remove the item
        self.__delitem__(self.heap_size-1)
        self.heap_size -=1
        #check if that value has broken sth
        max_heapify(self,0,self.heap_size-1)
        return maximum

    def increase_key(self,index,value,bigger=True):
        """
        Method just increases the value of index but
        it also checks if the current values is bigger
        than parent which makes it cool O(logn), the bigger
        here is a key thing beause when we append a new one
        we should give some dummy value to the new one so
        increase key may not work as usual ....(Think about it)
        """
        
        key = self.__getitem__(index)
        if key > value and bigger:
            raise Exception("The value should be bigger than key ,that is why is that")
        #set it
        #super(MaxHeap,self).__setitem__
        super(MaxHeap,self).__setitem__(index,value)

        while index > 0 and self.__getitem__(self.__get_parent_index(index)) < self.__getitem__(index):
            parent_index = self.__get_parent_index(index)
            tmp = self.__getitem__(parent_index)
            #print "The parent is : ",tmp
            super(MaxHeap,self).__setitem__(parent_index,self.__getitem__(index))
            super(MaxHeap,self).__setitem__(index,tmp)
            index = parent_index

   
    def __get_parent_index(self,index):
        """
        Simple parent getter
        """
        return (index-1)/2

    def new_delete(self,index):
        """
        New delete operation for heap
        """
        if self.heap_size < 1:
            raise Exception("The heap is empty sorry")
        
        #swap it with the latest one
        super(MaxHeap,self).__setitem__(index,self.__getitem__(self.heap_size-1))
        #remove the item
        self.__delitem__(self.heap_size-1)
        self.heap_size -=1
        if index == self.heap_size:
            return

        #print "Index is :",index
        #check firstly if it is bigger than its parent
        if (index > 0) and (self.__getitem__(self.__get_parent_index(index)) < self.__getitem__(index)):
            self.increase_key(index,self.__getitem__(index),bigger=False)
        else:#if not heapify to down
            max_heapify(self,index,self.heap_size-1)
            
  
    def __get_left(self,index):
        return index*2+1

    def __get_right(self,index):
        return index*2+2
    #######Normal list operations changed####

    def append(self,object):
        """
        Changed according to heap requirement try not to 
        use it,use instead insert_to_heap method
        """
        super(MaxHeap,self).append(object)
        self.rebuild_max_heap()

    def extend(self,iterable):
        """
        Changed according to heap requirement try not to 
        use it,use instead insert_to_heap method
        """

        super(MaxHeap,self).extend(iterable)
        self.rebuild_max_heap()
        

    def pop(self):
        """
        Changed according to heap requirement try not to 
        use it,use instead insert_to_heap method
        """ 
        super(MaxHeap,self).pop()
        self.rebuild_max_heap()

    def remove(self,value):
        """
        Changed according to heap requirement try not to 
        use it,use instead insert_to_heap method
        """
        super(MaxHeap,self).remove(value)
        self.rebuild_max_heap()
        

   
if __name__ == "__main__":
    m = MaxHeap([1,2,11,12,-1,33])
    #print m
    m.rebuild_max_heap()
    #print m.get_maximum()
    #print m.extract_max()
    #print m
    del m

    #now lets test the increase_key method
    m = MaxHeap([16,14,10,8,7,9,3,2,4,1])
    print m
    #m.increase_key(8,2)
    m.insert_to_heap(8)
    print m

    
