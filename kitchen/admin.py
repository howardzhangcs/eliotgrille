from django.contrib import admin

# Register your models here.

from kitchen.models import Inventory, Menu

admin.site.register(Inventory)
admin.site.register(Menu)
