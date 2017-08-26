from django.db import models


class Addressable(models.Model):
    class Meta:
        abstract = True
    street = models.CharField(max_length=255, blank=True)
        

class Restaurant(Addressable):
    class Meta:
        abstract = True

    # restaurant_addressable = models.OneToOneField(
    #     Addressable, parent_link=True, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=255)
    

class Bar(Restaurant):
    class Meta:
        abstract = True

    # bar_restaurant = models.OneToOneField(
    #     Restaurant, parent_link=True, on_delete=models.CASCADE)
    
    min_age = models.IntegerField()
    

class Pizzeria(Restaurant):
    
    # pizzeria_restaurant = models.OneToOneField(
    #     Restaurant, parent_link=True, on_delete=models.CASCADE)

    specialty = models.CharField(max_length=255)

    
class PizzeriaBar(Bar, Pizzeria):
    pizza_bar_specific_field = models.CharField(max_length=255)

    # pizzeriabar_pizzeria = models.OneToOneField(
    #     Pizzeria, parent_link=True, on_delete=models.CASCADE)

    # pizzeriabar_bar = models.OneToOneField(
    #     Bar, parent_link=True, on_delete=models.CASCADE)

