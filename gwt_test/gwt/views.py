# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Context, Template
from gwt_test.settings import TEMPLATE_DIRS 
from django.http import HttpResponse

import random
import os

def index(request):
    return render_to_response(
            'WithPlugin.html',
            {},
            context_instance=RequestContext(request)
            )



def gwt_xml(request):
    """
    Simple noway method
    """
    q = request.GET.get('q')
    stock_products = [t.strip() for t in q.split()]
    MAX_PRICE = 100
    MAX_CHANGE = 0.02

    xml_dict = {}
    for stock in stock_products:
        xml_dict[stock]={}
        price = random.randint(0,int(MAX_PRICE))
        change = price*random.randint(0,int(MAX_PRICE))/100*MAX_CHANGE
        xml_dict[stock]['price']=price
        xml_dict[stock]['change']=change
    
    #print "The final gwt data is ",xml_dict
    
    t = Template(open(os.path.join(TEMPLATE_DIRS[0],"gwt.xml"),"r").read())
    c = Context({
        'xml_dict':xml_dict
        })
    return HttpResponse(t.render(c),mimetype="application/xhtml+xml")

 

