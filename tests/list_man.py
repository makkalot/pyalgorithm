
class TList(list):

    def __init__(self,list_obj=None,get_name=None):
        self.get_name = get_name
        super(TList,self).__init__(list_obj)

    def __getitem__(self,index):
        tmp_var = super(TList,self).__getitem__(index)
        if not self.get_name:
            return tmp_var
        else:
            return getattr(tmp_var,self.get_name)

    def get_max(self):
        return super(TList,self).__getitem__(0)

def test_normal():
    x = [1,2,3,4]
    tl = TList(x)

    for e in tl:
        assert e == x[x.index(e)]

    print "Normal test passed"

def test_unnormal():
    class CusomList(object):
        def __init__(self,val):
            self.val = val

    x = [CusomList(1),CusomList(2),CusomList(3),CusomList(4)]
    tl = TList(x,"val")
    
    print "They are equal ? ",tl[0] == tl[1]
    print "Compar eem :",tl[2] > tl[3]
    print "The maix is ",tl.get_max()

    print "The unnormal test is passed"


