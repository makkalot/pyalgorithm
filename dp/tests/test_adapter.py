from pyalgorithm.dp.adapter import *

def test_adapter():

    #first test the old api
    tmp = [12,22,44]
    from copy import copy

    old=OldApiList(copy(tmp))
    old.add_new(20)
    tmp.append(20)

    assert old == tmp
    old.remove_first()
    tmp.remove(12)
    assert old == tmp

    old.remove_item(0)
    tmp.remove(22)
    assert old == tmp

    
    tmp = [12,22,44]
    new_api=NewApiStack(copy(tmp))
    x=new_api.pop()
    y=tmp.pop()
    assert new_api == tmp
    new_api.push_begin(88)
    tmp.insert(0,88)
    assert new_api == tmp


    tmp = [12,22,44]
    oa=OldToNewApi(copy(tmp))
    oa.add_new(66)
    print oa
    oa.remove_item(0)
    oa.remove_item(3)
    print oa
    #oa.remove_first() raises NotImplemented Error

