class Validator(object):
    """
    A simple class that validates some types,yes cool
    """
    def __init__(self,to_validate):
        self.obj = to_validate


    def validate(self,obj):
        """
        Should be overriden
        """
        raise NotImplementedError

class StringValidator(Validator):

    min_len = 10
    max_len = 20
    
    def validate(self):
        if len(self.obj) > self.max_len or len(self.obj)<self.min_len:
            raise Exception("The given string should be betweeen %s - %s "%(self.min_len,self.max_len))
        return self.obj

class IntegerValidator(Validator):

    integer_range=(0,100)
    def validate(self):
        if self.obj > self.integer_range[1] or self.obj<self.integer_range[0]:
            raise Exception("The given string should be betweeen %s - %s "%(self.integer_range[0],self.integer_range[1]))
        return self.obj

class Creator(object):
    """
    That will be the abstract creator actually those
    abstract implementations are not so cool in Python
    """
    def create(self,some_obj):
        raise NotImplementedError

class ValidatorFactory(Creator):
    
    def create(self,some_obj):
        if type(some_obj) == str:
            return StringValidator(some_obj)
        elif type(some_obj)==int:
            return IntegerValidator(some_obj)
        else:
            return None






