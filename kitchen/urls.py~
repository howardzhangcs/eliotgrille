from django.conf.urls import patterns, url, include

from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from kitchen import views

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    
    # login/logout
    url(r'^accounts/login/$', views.login, name = 'login'),
    url(r'^accounts/auth/$', views.auth_view, name = 'auth'),
    url(r'^accounts/logout/$', views.logout, name = 'logout'),
    url(r'^accounts/loggedin/$', views.loggedin, name = 'loggedin'),
    url(r'^accounts/invalid/$', views.invalid_login, name = 'invalid_login'),
    
    # employee
    url(r'^employee/$', views.employee, name = 'employee'),
    
    # inventory
    url(r'^inventory/$', login_required(views.InventoryView.as_view()), name='inventory'),
    url(r'^updateinven/$', login_required(views.UpdateView.as_view()), name='updateinven'),
    url(r'^u_inven/$', views.u_inven, name='u_inven'),
    
    url(r'^addinven/$', views.addinven, name='addinven'),
    url(r'^reminven/$', login_required(views.ReminvenView.as_view()), name='reminven'),
    url(r'^u_addinven/$', views.u_addinven, name='u_addinven'),
    url(r'^u_reminven/$', views.u_reminven, name='u_reminven'),
    
    # menu
    url(r'^menu/$', views.MenuView.as_view(), name='menu'),
    url(r'^addmenu/$', views.addmenu, name='addmenu'),
    url(r'^remmenu/$',  login_required(views.RemmenuView.as_view()), name='remmenu'),
    url(r'^u_addmenu/$', views.u_addmenu, name='u_addmenu'),
    url(r'^u_remmenu/$', views.u_remmenu, name='u_remmenu'),
    url(r'^updatemenu/$',  login_required(views.UpdateMenuView.as_view()), name='updatemenu'),
    url(r'^u_menu/$', views.u_menu, name='u_menu'),
    
    # success/failure
    url(r'^successresults/$', views.successresults, name='successresults'),
    url(r'^failresults/$', views.failresults, name='failresults'),
    #url(r'^order/$', views.orderView.as_view(), name='order'),
    #url(r'^currentorders/$', views.MUpdateView.as_view(), name='currentorders'),
)
