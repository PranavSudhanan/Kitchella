from app.models import Product, Category, Review, Customer, Store, Inventory
import random
products = Product.objects.all()
stores = Store.objects.all()
for product in products:
    for store in stores:
        inven = Inventory(quantity = random.randint(1, 100),
                          store = store,
                          product = product
                          )
        inven.save()