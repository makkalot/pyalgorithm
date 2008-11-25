class Subject(object):
    """
    That class is one that other want to follow
    when sth interesting happens.
    """
    def __init__(self):
        #these will be references to the
        self.observers = []

    def add_observer(self,observer_obj):
        """
        Method just adds a new observer here
        """
        if not isinstance(observer_obj,Observer):
            raise Exception("Only the types of Observer are allowed")

        if not observer_obj in self.observers:
            self.observers.append(observer_obj)

    def remove_observer(self,observer_obj):
        """
        Method just removes a subscriber
        """
        try:
            self.observers.remove(observer_obj)
        except ValueError,e:
            print e

    def notify_all(self):
        """
        Method will send the message to all that are registered here
        """
        for observer in self.observers:
            observer.update(self)#send yourself




class Observer(object):
    """
    The classes that inherits that one will be 
    the observers of it.
    """
    def update(self,subject_obj,**kwargs):
        """
        A method where observer objects can override and pull 
        the data they need
        """
        pass


class ConcreteSubject(Subject):
    """
    A concrete Subject for setting and notiying some 
    other objects ...
    """
    my_x = 0
    my_y = 0

    def values_changed(self):
        self.notify_all()

    def __str__(self):
        return "Here is my values %d and %d "%(self.my_x,self.my_y)

class ObserverX(Observer):
    """
    I will pull only the x
    """
    def update(self,subject_obj,**kwargs):
        print "Im X observer and got : ",subject_obj.my_x

class ObserverGeneral(Observer):
    
    def update(self,subject_obj,**kwargs):
        print "I got all of them ",str(subject_obj)


if __name__ == "__main__":
    pass
