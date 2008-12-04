from pyalgorithm.dp.command import *

def test_me_yo():
    """
    Lets see that one
    """
    tmp_file = open("some.txt","w")
    tmp_file.write("hehehe\n")
    tmp_file.close()

    #end of initial data
    #first lets read the contents of the stuff
    fe = FileEditor()
    fileman = FileMan("some.txt")
    fread = FileReadCommand(fileman)
    fwrite=FileWriteCommand(fileman)
    fe.set_command(fread)
    fe.process_command()

    #append some info to the end of it
    fe.set_command(fwrite)
    fe.process_command("add some text here")
    fe.set_command(fread)
    fe.process_command()

    #lets now go and create an command manager
    cm = CommanManager()
    cm.add_commanders(fwrite,fread)
    fe.set_command(cm)
    fe.process_command("\n Add another sting here ")
    
    print "First undo :"
    fe.undo_process()
    print "Second undo :"
    fe.undo_process()
    print "Thirrd undo :"
    fe.undo_process()

