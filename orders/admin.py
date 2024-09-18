from django.contrib import admin
from .models import Hotel, PizzaHut, Dominos, Toppings, OMR, NMR, Kapilavastu, Malabar, UserOrder, SavedCarts
from tinymce.widgets import TinyMCE
from django.db import models

class HotelAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.TextField: {'widget': TinyMCE()},
            }

class DominosAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.TextField: {'widget': TinyMCE()},
            }

class PizzaHutAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.TextField: {'widget': TinyMCE()},
            }


admin.site.register(Hotel,HotelAdmin)
admin.site.register(Dominos, DominosAdmin)
admin.site.register(PizzaHut, PizzaHutAdmin)
admin.site.register(Toppings)
admin.site.register(OMR)
admin.site.register(NMR)
admin.site.register(Malabar)
admin.site.register(Kapilavastu)
admin.site.register(UserOrder)
admin.site.register(SavedCarts)
