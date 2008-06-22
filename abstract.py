#the main structure of an algortihm

class AbstractAlgorithm :
        
    name = "The name of the algorithm"
    o_notation = "The O(n) notation of the algo"

    def __init__(self,*args,**kw):
        pass

    def implement(self):
        """ This is the real implementation"""
        pass


if __name__=="__main__":
    pass
