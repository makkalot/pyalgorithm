#That program claims to be a solution to historical cigarette smokers problem
#which is a very famous one for University students. The problem can be found 
#from here [LINK]. It may not be the best solution but as far i tested it didnt recognize
#any deadlocks or some other evil things in multi-threaded programming :) Enjoy it...

from threading import *
import time
import thread

#table condition True means you can put ingredients there False means you cant
NUM_OF_SMOKERS = 3

class Smoker(Thread):
    """
    The smoker class that has only one 
    of the ingredients
    """
    MAX_SMOKE_SEC = 20.0

    def __init__(self,id):
        """
        Initializer ...
        """
        Thread.__init__(self)
        #the table variables
        self.id =id
        #the smoker turn things
        self.now_smoking = False
        #the start time of smoking
        self.start_time = None
    
    def do_i_smoke(self):
        """
        A simple util that tells to the Thread if it is still smoking :)
        funny illusion ...
        """
        if not self.now_smoking or not self.start_time:
            return False

        dif = float(time.time())-float(self.start_time)
        if dif > self.MAX_SMOKE_SEC:
            print "Im %d of smokers and i finished smoking ..."%(self.id)
            self.now_smoking = False
            return False
        else:
            return True

    def run(self):
        """
        The real running part for that Thread
        """
        global table_cond
        global smoke_lock
        global smoke_turn

        while 1:
            smoke_lock.acquire()
            #if it is not my turn i will wait and release the lock or if im
            #smoking now icant get a second cigarette right :)
            
            while self.id != smoke_turn or self.now_smoking == True:
                #print "Im the %d HI and the turn is %d and do i smoke %s"%(self.id,smoke_turn,self.now_smoking)
                if self.id == smoke_turn and self.now_smoking == True:
                    if self.do_i_smoke(): #if True i'm still smoking
                        print "Im %d and still smoking sorry :)"%(self.id)
                        table_cond = True
                        #notify him to choose a new one yo !
                        smoke_lock.notifyAll()
                    else:
                        #if you are not smoking than you should try sth different
                        continue
                
                smoke_lock.wait()
        

            print "Im %d  took the ingrediens and will signal arbiter"%(self.id)
            #he/she started to smoke :)
            self.start_time = time.time()
            self.now_smoking = True
            print "Im %d and i will smoke for %d seconds"%(self.id,self.MAX_SMOKE_SEC)
            smoke_turn = -1
            #tell to arbiter that he can give to others
            table_cond = True
            smoke_lock.notifyAll()
            smoke_lock.release()
            #you can release the lock now


class Arbiter(Thread):
    """
    The arbiter that gives to others the ingredients to smoke
    """

    def __init__(self,id):
        Thread.__init__(self)
        self.id = id

    def __choose_smoker(self):
        import random
        
        chosen = []
        while len(chosen) != NUM_OF_SMOKERS:
            tmp = random.randint(0,NUM_OF_SMOKERS-1)
            if not tmp in chosen:
                chosen.append(tmp)

        #get the one you have chosen randomly !
        return chosen[len(chosen)-1]

    def run(self):
        """
        The real part :)
        """
        #get the lock
        global smoke_lock
        global table_cond
        global smoke_turn

        while 1:
            #get the lock
            smoke_lock.acquire()
            
            #if there is sth on the table you should wait until sone
            #takes them from there ...
            while table_cond == False:
                smoke_lock.wait()

            #get the new smoker a simple random operation
            tmp_chose = self.__choose_smoker()
            print "Im arbitter %d and chosen to smoke the %d and will notify Him"%(self.id,tmp_chose)
            #that sleep is just for seeing things better and slower
            time.sleep(5)

            #we have now a new turn
            smoke_turn = tmp_chose
            #the table is full so ...
            table_cond = False
            
            #tell all that you chose somebody
            smoke_lock.notifyAll()
            #release the lock here
            smoke_lock.release()

if __name__ == "__main__":
    #a list for smoker threads
    smokers = []
    #give the first turn to the Arbiter
    table_cond = True
    smoke_lock = Condition()
    smoke_turn = -1 #none
    #create the therads
    for i in xrange(0,NUM_OF_SMOKERS):
        tmp = Smoker(i)
        smokers.append(tmp)

    #create the arbitter
    ar = Arbiter(NUM_OF_SMOKERS+1)
    smokers.append(ar)
    
    #start all of them
    for th in smokers:
        th.start()

    #wait to JOIN all, they wont actually
    #they will smoke forever ...
    for th in smokers:
        th.join()

