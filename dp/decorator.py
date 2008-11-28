#Python already has a decorator method but that one here maybe a little bit different

class FileReader(object):
    """
    A simple method that opens and closes files
    """
    def __init__(self,fname):
        self.file = open(fname,"r")

    def read_content(self):
        """
        I made it blank intentionally to be overriden
        """
        pass

    def close_file(self):
        self.file.close()


class NormalFileReader(FileReader):
    """
    That one will simply got the contents of the file
    """
    
    def read_content(self):
        """
        I made it blank intentionally to be overriden
        """
        return self.file.read()


class DecoratoClass(FileReader):
    def __init__(self,file_reader):
        """
        The constructor recieves a file reader as a parameter
        """
        self.file_reader = file_reader


class DecoratoUpperFileReader(DecoratoClass):
    """
    The contents will be converted to Upper case
    """
    
    def read_content(self):
        return str(self.file_reader.read_content()).upper()



class DecoratoSha1Reader(DecoratoClass):
    """
    The contents will be converted to sha1sum
    """
    def read_content(self):
        from sha import sha
        digest_handler = sha()
        digest_handler.update(str(self.file_reader.read_content()))
        return digest_handler.hexdigest()


