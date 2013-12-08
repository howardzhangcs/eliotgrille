from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from kitchen.models import Order
from django.utils import timezone
from django.core import serializers
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

@dajaxice_register
def temp_add_order(req, form):
    dajax = Dajax()
    p = form['food']
    n = int(form['quantity'])
    if n == 0:
        dajax.alert("You Selected a Zero Quantity")
    else:
        m = Order(order_food = p, order_quantity = n, is_currentorder = True, dateofentry = timezone.now())
        m.save() 
        dajax.redirect(reverse('employee'), delay=0)
    return dajax.json()

@dajaxice_register
def temp_delete_order(req, form):
    dajax = Dajax()
    p = Order.objects.get(pk=int(form))
    p.is_currentorder = False
    p.save()
    dajax.redirect(reverse('employee'), delay=0)
    return dajax.json()
