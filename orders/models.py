from django.db import models
from datetime import datetime

# Create your models here.

class Hotel(models.Model):
    category_title = models.CharField(max_length=200)
    category_gif = models.CharField(max_length=200)
    category_description = models.TextField() #make this the wysiwyg text field
    rating = models.DecimalField(default=0, max_digits=1, decimal_places=1)
    def __str__(self):
        #overriding the string method to get a good representation of it in string format
        return f"{self.category_title}"



class PizzaHut(models.Model):
    #example row :: 1 topping , 5.00 , 7.00
    pizza_choice = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=1)
    rating = models.PositiveIntegerField(default=0)
    img = models.CharField(max_length=200, default = "/orders/images/pizzahut/burger_pizza.jpg")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category_description = models.TextField() #make this the wysiwyg text field

    def __str__(self):
        #overriding the string method to get a good representation of it in string format
        return f"PizzaHut: {self.pizza_choice}"

class Dominos(models.Model):
    #example row :: 1 topping , 5.00 , 7.00
    pizza_choice = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=1)
    rating = models.PositiveIntegerField(default=0)
    img = models.CharField(max_length=200, default = "/orders/images/dominos/morocco_pizza.jpg")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category_description = models.TextField() #make this the wysiwyg text field

    def __str__(self):
        #overriding the string method to get a good representation of it in string format
        return f"Dominos : {self.pizza_choice}"

class Toppings(models.Model):
    #example row :: Pepperoni
    topping_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    

    def __str__(self):
        #overriding the string method to get a good representation of it in string format
        return f"{self.topping_name}"


class OMR(models.Model):
    #example row :: meatball , 5.00 , 6.50
    sub_filling = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=1)
    rating = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    img = models.CharField(max_length=200, default = "/orders/images/omr/sausage.jpg")
    def __str__(self):
        #overriding the string method to get a good representation of it in string format
        return f"OMR : {self.sub_filling}"

class NMR(models.Model):
    dish_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=1)
    rating = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    img = models.CharField(max_length=200) 
    def __str__(self):
        #overriding the string method to get a good representation of it in string format
        return f"NMR {self.dish_name}"


class Kapilavastu(models.Model):
    dish_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=1)
    rating = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    img = models.CharField(max_length=200,default ="/orders/images/kapilavastu/avocado.jpg") 
    def __str__(self):
        #overriding the string method to get a good representation of it in string format
        return f"Kapilavastu : {self.dish_name}"



class Malabar(models.Model):
    dish_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=1)
    rating = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    img = models.CharField(max_length=200,default ="/orders/images/malabar/avocado.jpg") 

    def __str__(self):
        #overriding the string method to get a good representation of it in string format
        return f"Malabar : {self.dish_name}"

class UserOrder(models.Model):
    username = models.CharField(max_length=200) #who placed the order
    order = models.TextField() #this will be a string representation of the cart from localStorage
    price = models.DecimalField(max_digits=6, decimal_places=2) #how much was the order
    time_of_order  = models.DateTimeField(default=datetime.now, blank=True)
    delivered = models.BooleanField()

    def __str__(self):
        #overriding the string method to get a good representation of it in string format
        return f"Order placed by  : {self.username} on {self.time_of_order.date()} at {self.time_of_order.time().strftime('%H:%M:%S')}"

class SavedCarts(models.Model):
    username = models.CharField(max_length=200, primary_key=True)
    cart = models.TextField() #this will be a string representation of the cart from localStorage

    def __str__(self):
        #overriding the string method to get a good representation of it in string format
        return f"Saved cart for {self.username}"
