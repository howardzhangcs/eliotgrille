from django.conf.urls import patterns, url, include

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

    #inventory
    url(r'^inventory/$', views.InventoryView.as_view(), name='inventory'),
    url(r'^updateinven/$', views.UpdateView.as_view(), name='updateinven'),
    url(r'^u_inven/$', views.u_inven, name='u_inven'),
    url(r'^successresults/$', views.successresults, name='successresults'),
    url(r'^failresults/$', views.failresults, name='failresults'),
    url(r'^menu/$', views.MenuView.as_view(), name='menu'),
    url(r'^addinven/$', views.addinven, name='addinven'),
    url(r'^reminven/$', views.ReminvenView.as_view(), name='reminven'),
    url(r'^u_addinven/$', views.u_addinven, name='u_addinven'),
    url(r'^u_reminven/$', views.u_reminven, name='u_reminven'),
    url(r'^addmenu/$', views.addmenu, name='addmenu'),
    url(r'^remmenu/$', views.RemmenuView.as_view(), name='remmenu'),
    url(r'^u_addmenu/$', views.u_addmenu, name='u_addmenu'),
    url(r'^u_remmenu/$', views.u_remmenu, name='u_remmenu'),
    url(r'^updatemenu/$', views.UpdateMenuView.as_view(), name='updatemenu'),
    url(r'^u_menu/$', views.u_menu, name='u_menu'),
    #url(r'^order/$', views.orderView.as_view(), name='order'),
    #url(r'^currentorders/$', views.MUpdateView.as_view(), name='currentorders'),
)
