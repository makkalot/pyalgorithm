class Singleton(object):
    __instance = None

    def __new__(cls,*args,**kwargs):
        """
        Override the instantiation of the object
        """
        if not cls.__instance or type(cls.__instance)!=cls:
            import time
            time.sleep(5)
            cls.__instance = object.__new__(cls,*args,**kwargs)
            print "Creating new instance ",cls.__instance
        return cls.__instance


    def destroy(self):
        Singleton.__instance=None

