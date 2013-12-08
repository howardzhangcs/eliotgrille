from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from django.forms import CreateAddForm

@dajaxice_register
def temp_add_order(request, form):
    add_form = CreateAddForm(deserialize_form(form))
    if add_form.is_valid():
	    p = add_form.cleaned_data['order_food']
        n = add_form.cleaned_data['order_quantity']	
	    m = Order(order_food = p, order_quantity = n, is_currentorder = True, dateofentry = timezone.now())
        latest_order_list = Order.objects.get(is_create=True)
        return simplejson.dumps({'latest_order_list': latest_order_list})
