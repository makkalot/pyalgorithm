from pyalgorithm.dp.state import *
import unittest

class TestAbstractState(unittest.TestCase):

    def setUp(self):
        self.product = Product(self.get_current_state(),4,self.get_current_date())
        self.context = ProductContext(self.product)

    def get_current_state(self):
        return DELETED_STATE 

    def get_current_date(self):
        import datetime 
        ex_date = datetime.datetime.now()
        return ex_date

    def test_moderate_product(self,**kwargs):
        self.assertRaises(NotImplementedError,self.context.moderate_product)

    def test_fix_product(self,**kwargs):
        self.assertRaises(NotImplementedError,self.context.fix_product)

    def test_sell_product(self,**kwargs):
        self.assertRaises(NotImplementedError,self.context.sell_product)

    def test_refill(self,**kwargs):
        self.assertRaises(NotImplementedError,self.context.refill)
    
    def test_return_cancel_item(self,**kwargs):
        self.assertRaises(NotImplementedError,self.context.return_cancel_item)

class NotActiveState(TestAbstractState):

    def get_current_state(self):
        return NOT_ACTIVE_STATE

    def test_moderate_product(self):
        print self.context.current_state
        try:
            self.context.moderate_product()
        except Exception,e:
            print e

        self.context.moderate_product(moderate_result=True)
        assert self.context.product.state == UNDER_MODERATION_STATE

