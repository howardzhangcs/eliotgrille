from django.db import models

# Create your models here.

#Inventory Model
class Inventory(models.Model):
    material = models.CharField(unique=True, max_length=200)
    stock_material = models.PositiveIntegerField(default=0)
    dateofentry = models.DateTimeField('date published')
    def __unicode__(self):
        return self.material

#Menu Model
class Menu(models.Model):
    food = models.CharField(unique=True, max_length=200)
    price_food = models.DecimalField(max_digits = 4, decimal_places = 2, default=0.00)
    dateofentry = models.DateTimeField('date published')
    def __unicode__(self):
        return self.food

#Order Model
class Order(models.Model):
    order_food = models.CharField(unique=True, max_length=200)
    order_quantity = models.DecimalField(max_digits = 4, decimal_places = 2, default=0.00)
    dateofentry = models.DateTimeField('date published')
    def __unicode__(self):
        return self.order_food

