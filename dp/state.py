NOT_ACTIVE_STATE=0
UNDER_MODERATION_STATE = 1
REJECTED_STATE = 2
ACTIVE_STATE = 3
DELETED_STATE = 4
OUT_OF_STATE = 5

class Product(object):
    """
    The object we are working on
    """
    def __init__(self,state,items,expire_date):
        self.items = items
        self.state = state
        self.expire_date=expire_date



class AbstractProductState(object):
    
    def __init__(self,context):
        self.context = context

    def moderate_product(self,**kwargs):
        raise NotImplementedError

    def fix_product(self,**kwargs):
        raise NotImplementedError

    def sell_product(self,**kwargs):
        raise NotImplementedError

    def refill(self,**kwargs):
        raise NotImplementedError
    
    def return_cancel_item(self,**kwargs):
        raise NotImplementedError


    def delete_product(self,**kwargs):
        """
        Deletes a product which is under moderation and option also
        """
        self.context.set_state(DELETED_STATE)



class NotActiveState(AbstractProductState):
    """
    When a product is not active
    """
    def moderate_product(self,**kwargs):
        if kwargs.has_key('moderate_result'):
            if kwargs['moderate_result']:
                self.context.set_state(UNDER_MODERATION_STATE)
        else:
            raise Exception("Error in moderation")



class UnderModerationState(AbstractProductState):
    """
    When a product is under moderation 
    """
    def moderate_product(self,**kwargs):
        if kwargs.has_key('moderate_result'):
            if kwargs['moderate_result']:
                self.context.set_state(ACTIVE_STATE)
            else:
                self.context.set_state(REJECTED_STATE)
        else:
            raise Exception("Error in moderation")

  
class RejectedState(AbstractProductState):
    """
    When a project is rejected
    """
    def fix_product(self,**kwargs):
        self.context.set_state(UNDER_MODERATION_STATE)

CAN_NOT_DELETE = 60*60 #that is the time when a use can not delete a product
class ActiveState(AbstractProductState):
    """
    When a product is active for selling and oher actions
    """
    def moderate_product(self,**kwargs):
        if kwargs.has_key('moderate_result'):
            if kwargs['moderate_result']:
                self.context.set_state(UNDER_MODERATION_STATE)
        else:
            raise Exception("Error in moderation")
        
    def return_cancel_item(self,**kwargs):
        if kwargs.has_key('return_cancel_item'):
            self.context.product.items +=1

        else:
            raise Exception("Error in return_cancel_item method")

    def sell_product(self,**kwargs):
        if kwargs.has_key('sell_product'):
            if kwargs['sell_product']:
                self.context.product.items -= 1
                if not self.context.product.items > 0 :
                    #its state is now out of sale
                    self.context.set_state(OUT_OF_STATE)
        else:
            raise Exception("Error in moderation")
            

    def fix_product(self,**kwargs):
        """
        Yes user can fix the product when it is active
        """
        pass
    
    def delete_product(self,**kwargs):
        """
        Deletes a product which is under moderation and option also
        """
        import datetime
        now = datetime.datetime.now()
        if not CAN_NOT_DELETE >(self.product.expire_date - now):
            self.context.set_state(DELETED_STATE)
        else:
            raise Exception("You can not delete a project when there is less than ...")

class DeletedState(AbstractProductState):
    """
    When a product is deleted by administration you can not do anything :)
    """
    pass

class OutOfSaleSatet(AbstractProductState):
    """
    When a product is finished 
    """
    def refill(self,**kwargs):
        if kwargs.has_key('items'):
            self.context.product.items += kwargs['items']
            self.convert.set_state(ACTIVE_STATE)
        else:
            raise Exception("Method args error here...")
    
    def return_cancel_item(self,**kwargs):
        if kwargs.has_key('return_cancel_item'):
            self.context.product.items +=1
            self.convert.set_state(ACTIVE_STATE)
        else:
            raise Exception("Error in return_cancel_item method")


class ProductContext(object):
        
    states = {
            NOT_ACTIVE_STATE:NotActiveState,
            UNDER_MODERATION_STATE:UnderModerationState,
            REJECTED_STATE:RejectedState,
            ACTIVE_STATE:ActiveState,
            DELETED_STATE:DeletedState,
            OUT_OF_STATE:OutOfSaleSatet
            }
        
    def __init__(self,product):
        self.product = product
        self.current_state = self.set_state(product.state)

    def set_state(self,string_state):
        """
        because the ones in products are strings we should convert to objects
        """
        if self.states.has_key(string_state):
            #set aldo the product
            self.product.state=string_state
            return self.states[string_state](self)
        else:
            return None
        
    def moderate_product(self,**kwargs):
        self.current_state.moderate_product(**kwargs)

    def fix_product(self,**kwargs):
        self.current_state.fix_product(**kwargs)

    def sell_product(self,**kwargs):
        self.current_state.sell_product(**kwargs)

    def refill(self,**kwargs):
        self.current_state.refill()
    
    def return_cancel_item(self,**kwargs):
        self.current_state.return_cancel_item(**kwargs)


    def delete_product(self,**kwargs):
        """
        Deletes a product which is under moderation and option also
        """
        self.current_state.delete_product(**kwargs)


