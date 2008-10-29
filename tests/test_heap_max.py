from pyalgorithm.util import *
from pyalgorithm.max_priority_heap import MaxHeap

class TestMaxHeap(object):
    """
    A test class to test heap operations here
    """

    def rebuild_all(self):
        from copy import copy
        tmp_unique = generate_unique(0,10000,1000)
        self.real_heap = MaxHeap(tmp_unique)
        self.copy_heap = copy(self.real_heap)

    def test_insert(self):
        """
        Insert 100 elements
        """
        self.rebuild_all()
        import random
        for i in xrange(0,100):
            tmp = random.randint(0,10000)
            self.real_heap.insert_to_heap(tmp)
            assert self.is_heap_valid(self.real_heap) == True
           
            tmp_max = max(self.real_heap)
            real_max = self.real_heap.extract_max()
            assert tmp_max == real_max
            assert self.is_heap_valid(self.real_heap) == True


            if i%10==0:
                print "Insertion of %d/%d is completed"%(i,100)


    def is_heap_valid(self,heap_candidate):
        l = len(heap_candidate)
        for member in xrange(0,l):
            left = member*2+1
            rigth = member*2+2

            if not left >= l:
                if heap_candidate[member] < heap_candidate[left]:
                    #print "Left"
                    #print heap_candidate[member]
                    #print heap_candidate[left]
                    #print heap_candidate
                    return False

            if not rigth >=l:
                
                if heap_candidate[member] < heap_candidate[rigth]:
                    #print "Rigth"
                    #print heap_candidate[member]
                    #print heap_candidate[rigth]
                    #print heap_candidate
                    return False

        return True

    def test_deleter(self):
        """
        Delete all elements one by one
        """
        self.rebuild_all()
        l = len(self.real_heap)
        #print "Before :",l
        for member_remove in xrange(0,l):
            self.rebuild_all()
            
            l = len(self.real_heap)
            #print "Aftre :",l
            #print "To delete :",self.real_heap
            #print "member to delete :",member_remove
            self.real_heap.new_delete(member_remove)
            assert self.is_heap_valid(self.real_heap) == True

            #check if it is there ?
            tmp_max = max(self.real_heap)
            real_max = self.real_heap.extract_max()
            assert tmp_max == real_max
            assert self.is_heap_valid(self.real_heap) == True

            if member_remove%10==0:
                print "Deletion of %d/%d is completed"%(member_remove,l)

    
    def test_extract_max(self):
        """
        Test it 100 times
        """
        for i in xrange(0,100):
            self.rebuild_all()
            real_max = self.real_heap.extract_max()
            #print "real max is :",real_max
            #print "the copy max is :",max(self.copy_heap)
            assert real_max == max(self.copy_heap)
            assert self.is_heap_valid(self.real_heap) == True
            
            if i%10==0:
                print "Extraction of %d/%d is completed"%(i,100)

 
if __name__ == "__main__":
    t=TestMaxHeap()
    t.test_insert()
    t.test_deleter()
    t.test_extract_max()


            


