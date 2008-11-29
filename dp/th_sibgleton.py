import thread
class ThSingleton(object):
    __lockObj = thread.allocate_lock()  # lock object
    __instance = None

    def __new__(cls,*args,**kwargs):
        """
        Override the instantiation of the object
        """
        cls.__lockObj.acquire()
        if not cls.__instance or type(cls.__instance)!=cls:
            import time
            time.sleep(5)
            cls.__instance = object.__new__(cls,*args,**kwargs)
            print "Creating new instance ",cls.__instance
        cls.__lockObj.release()

        return cls.__instance


    def destroy(self):
        ThSingleton.__instance=None

