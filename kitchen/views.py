from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from kitchen.models import Inventory, Menu, Order
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.db.utils import IntegrityError
from django.contrib import auth
from django.core.context_processors import csrf 
from django.contrib.auth.decorators import login_required

##################################GENERAL##############################

#Index
def index(request):
    return redirect('menu')

#Index for employees
class EmployeeView(generic.ListView):
    template_name = 'kitchen/employee.html'
    context_object_name = 'latest_order_list'
    def get_queryset(self):
        return Order.objects.all()

#Success
@login_required(login_url='/accounts/login/')
def successresults(request):
    return render(request, 'kitchen/successresults.html')

#Failure
@login_required(login_url='/accounts/login/')
def failresults(request):
    return render(request, 'kitchen/failresults.html')

#view for Login
#http://www.youtube.com/watch?v=CFypO_LNmcc
def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'kitchen/login.html', c)

#logic for Login
#http://www.djangobook.com/en/2.0/chapter14.html
def auth_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('loggedin'))
    else:
        return HttpResponseRedirect(reverse('invalid_login'))

#display successful login
def loggedin(request):
    return render(request, 'kitchen/loggedin.html', {'full_name': request.user.username})

#display failed login
def invalid_login(request):
    return render(request, 'kitchen/invalid_login.html')

#Logout
def logout(request):
    auth.logout(request)
    return render(request, 'kitchen/logout.html')

########################################################################


#####################DISPLAY FOR INVENTORY#######################################

#site to view Inventory
class InventoryView(generic.ListView):
    template_name = 'kitchen/inventory.html'
    context_object_name = 'latest_inventory_list'
    def get_queryset(self):
        return Inventory.objects.all()

#site to change quantity of Inventory
class UpdateView(generic.ListView):
    template_name = 'kitchen/updateinven.html'
    context_object_name = 'latest_inventory_list'
    def get_queryset(self):
        return Inventory.objects.all()

#site to add new item to inventory
@login_required(login_url='/accounts/login/')
def addinven(request):
    return render(request, 'kitchen/addinven.html')

#site to remove item from inventory
class ReminvenView(generic.ListView):
    template_name = 'kitchen/reminven.html'
    context_object_name = 'latest_inventory_list'
    def get_queryset(self):
        return Inventory.objects.all()
####################################################################################


###################PROCESSING FOR INVENTORY#########################################

#Updates the quantity of Inventory
@login_required(login_url='/accounts/login/')
def u_inven(request):
    p = Inventory.objects.get(material=request.POST['ingredient'])
    try: 
        n = int(request.POST['quantity'])
    except ValueError:
        return HttpResponseRedirect(reverse('failresults'))
    if n == 0 or p.stock_material + n < 0:
        return HttpResponseRedirect(reverse('failresults'))
    else:
        p.stock_material += int(request.POST['quantity'])
        p.save()
        return HttpResponseRedirect(reverse('successresults'))

#Updates the addition of a new item to Inventory
@login_required(login_url='/accounts/login/')
def u_addinven(request):
    p = request.POST['ingredient']
    try:
        n = int(request.POST['quantity'])
    except ValueError:
        return HttpResponseRedirect(reverse('failresults')) 
    if  n < 0 or n > 99:
        return HttpResponseRedirect(reverse('failresults'))
    else:
        try:       
            m = Inventory(material = p, stock_material = n, dateofentry = timezone.now())
            m.save()
            return HttpResponseRedirect(reverse('successresults'))
	except IntegrityError:
	    return HttpResponseRedirect(reverse('failresults'))

#Updates the removal of an existing item from Inventory
@login_required(login_url='/accounts/login/')
def u_reminven(request):
    Inventory.objects.filter(material=request.POST['ingredient']).delete()
    return HttpResponseRedirect(reverse('successresults'))

###################################################################################################


###################################DISPLAY FOR MENU################################################

#site to view menu
class MenuView(generic.ListView):
    template_name = 'kitchen/menu.html'
    context_object_name = 'latest_menu_list'
    def get_queryset(self):
        return Menu.objects.all()

#site to add food to menu
@login_required(login_url='/accounts/login/')
def addmenu(request):
    return render(request, 'kitchen/addmenu.html')

#site to remove food from menu
class RemmenuView(generic.ListView):
    template_name = 'kitchen/remmenu.html'
    context_object_name = 'latest_menu_list'
    def get_queryset(self):
        return Menu.objects.all()

#site to update price in menu
class UpdateMenuView(generic.ListView):
    template_name = 'kitchen/updatemenu.html'
    context_object_name = 'latest_menu_list'
    def get_queryset(self):
        return Menu.objects.all()
#######################################################################################


#######################PROCESSING FOR MENU#############################################

#Updates the addition of new food to menu)
@login_required(login_url='/accounts/login/')
def u_addmenu(request):
    p = request.POST['food']
    try:
        n = float(request.POST['price'])
    except ValueError:
        return HttpResponseRedirect(reverse('failresults'))      
    if  n < 0 or n > 99:
        return HttpResponseRedirect(reverse('failresults')) 
    else:
        try:
            m = Menu(food = p, price_food = n, dateofentry = timezone.now())
            m.save()
            return HttpResponseRedirect(reverse('successresults'))
	except IntegrityError:
  	    return HttpResponseRedirect(reverse('failresults'))

#Updates the removal of existing food from menu
@login_required(login_url='/accounts/login/')
def u_remmenu(request):
    Menu.objects.filter(food=request.POST['food']).delete()
    return HttpResponseRedirect(reverse('successresults'))

#Updates the change in price in menu
@login_required(login_url='/accounts/login/')
def u_menu(request):
    p = Menu.objects.get(food=request.POST['food'])
    try:
        n = float(request.POST['price'])
    except ValueError:
        return HttpResponseRedirect(reverse('failresults'))
    if n < 0 or n > 99:
        return HttpResponseRedirect(reverse('failresults'))
    else:
        try:
            p.price_food = float(request.POST['price'])
            p.save()
	    return HttpResponseRedirect(reverse('successresults'))
        except IntegrityError:
	    return HttpResponseRedirect(reverse('failresults'))

#######################################################################################


####################Ordering for Kitchen#######################################
#displays site to make order
class MakeOrderView(generic.ListView):    
    template_name = 'kitchen/makeorder.html'
    context_object_name = 'latest_menu_list'
    def get_queryset(self):
        return Menu.objects.all()

@login_required(login_url='/accounts/login/')
def u_makeorder(request):
    p = request.POST['food']
    try:
        n = int(request.POST['quantity'])
    except ValueError:
        return HttpResponseRedirect(reverse('failresults'))      
    if  n < 0 or n > 99:
        return HttpResponseRedirect(reverse('failresults')) 
    else:
        try:
            m = Order(order_food = p, order_quantity = n, is_currentorder = True, dateofentry = timezone.now())
            m.save()
            return HttpResponseRedirect(reverse('successresults'))
	except IntegrityError:
  	    return HttpResponseRedirect(reverse('failresults'))

