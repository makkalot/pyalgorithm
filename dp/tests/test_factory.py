from pyalgorithm.dp.factory import *

def test_facto():
    my_value = "Some_strrrrrrrrr"
    factory = ValidatorFactory()
    validator = factory.create(my_value)
    print validator.validate()

    my_value = 11
    validator = factory.create(my_value)
    print validator.validate()

    my_value = 11.12
    validator = factory.create(my_value)
    if not validator:
        print "No object created ..."
    #print validator.validate()

