from app.models import *

for review in Review.objects.all():
    for store in Store.objects.all():
        print(Inventory.objects.get(product = review.product, store = store))