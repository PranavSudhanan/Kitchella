from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Inventory)
admin.site.register(Product)
admin.site.register(Salesperson)
admin.site.register(Store)
admin.site.register(Region)
admin.site.register(Customer)
admin.site.register(Transaction)
admin.site.register(TransactionItem)
admin.site.register(Review)
admin.site.register(CartItem)
