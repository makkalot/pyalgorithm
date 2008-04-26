#the main structure of an algortihm

class AbstractAlgorithm :

    def __init__(self):

        self.name = "The name of the algorithm"
        self.O = "The O(n) notation of the algo"
        self.time = "The time to accomplish its task"


    def implement(alg_obj):
        """ This is the real implementation"""
        pass

    def compute_time(alg_obj):
        """ That one computes the time"""
        pass

    def compute_memory(alg_obj):
        """ That one computes the memory needed """
        pass

if __name__=="__main__":
    pass
