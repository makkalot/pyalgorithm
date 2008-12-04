class FileEditor(object):
    """
    Some invoker class that will handle requestst
    """

    def set_command(self,command_object):
        self.command_object = command_object


    def process_command(self,string_process=None):
        """
        Here we call the command object
        """
        self.command_object(string_process) #some sugar pythonic

    def undo_process(self):
        self.command_object.undo()


class FileMan(object):
    """
    Some file operator for simple things
    """

    def __init__(self,fname):
        self.fname = fname
        self.file = None

    def append_line(self,some_str):
        """
        Appends a file
        """
        if not self.file:
            self.file = open(self.fname,"a")
        self.file.write(str(some_str))
        self.close_it()

    def write(self,some_str):
        if not self.file:
            self.file = open(self.fname,"w")
        self.file.write(some_str)
        self.close_it()


    def read_all(self):
        if not self.file:
            self.file = open(self.fname,"r")
        s=str(self.file.read())
        self.close_it()
        return s

    def print_all(self):
        print self.read_all()

    def close_it(self):
        if self.file:
            self.file.close()
        self.file = None
        
class Command(object):
    """
    A prototype for commands
    """
    def __init__(self,request_object=None):
        self.request_object = request_object

class FileReadCommand(Command):

    def __call__(self,some_str=None):
        self.request_object.print_all()

    def undo(self):
        pass


class FileWriteCommand(Command):
    
    previous_strings = []

    def __call__(self,str_write=None):
        self.request_object.append_line(str_write)
        self.previous_strings.append(str(str_write))


    def undo(self):
        if not self.previous_strings:
            print "Nothing to undo "
        else:
            all_str = self.request_object.read_all()
            to_undo = self.previous_strings.pop()

            index = all_str.find(to_undo)
            if index != -1:
                self.request_object.write(all_str[:index])


#Lets do some magic with those people
class CommanManager(Command):
    
    commanders = []
    def add_commanders(self,*args):
        self.commanders.extend(args)

    def __call__(self,some_str=None):

        for command in self.commanders:
            command(some_str)

    def undo(self):
        """
        Will do sth different here
        """
        self.commanders[0].undo()
        self.commanders[1]() #to print the contents




