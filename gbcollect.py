import gc
from collections import defaultdict

def classify():
    counters = defaultdict(lambda:0)
    for o in gc.get_objects():
        print o
        counters[type(o)] += 1
        counters = [(freq, t) for t,freq in counters.items()]
        counters.sort()
        
        for freq,t in counters[-10:]:
            print t.__name__, freq


if __name__=="__main__":

    print "I will allocate a lotofo strings :"
    classify()
    str = "a"*10000
    classify()
    print "Deleting the reference here"
    del str
    collections()


