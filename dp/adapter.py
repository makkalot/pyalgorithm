class OldApiList(list):
    
    def add_new(self,element):
        super(OldApiList,self).append(element)


    def remove_first(self):
        """
        Removes the 0 element
        """
        x=self[0]
        super(OldApiList,self).remove(x)

    def remove_item(self,index):
        x = self[index]
        super(OldApiList,self).remove(x)


class NewApiStack(list):

    def pop(self):
        return super(NewApiStack,self).pop()

    def push_begin(self,element):
        super(NewApiStack,self).insert(0,element)


class OldToNewApi(OldApiList):

    def __init__(self,*args,**kwarg):
        super(OldApiList,self).__init__(*args,**kwarg)
        self.adaptee = NewApiStack(*args,**kwarg)
        
    def add_new(self,element):
        self.adaptee.push_begin(element)

    def remove_first(self):
        """
        Removes the 0 element
        """
        raise NotImplementedError

    def remove_item(self,index):
        if index == len(self.adaptee)-1:
            return self.adaptee.pop()

        else:
            print "New implementation remove only the last one"
    
    def __str__(self):
        return str(self.adaptee) 



