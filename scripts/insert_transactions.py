from app.models import *
import random
import pandas
import datetime
from django.contrib.auth.models import Permission
from django.db.models import Q

perm = Permission.objects.get(codename='region_manager')
salespersons = Salesperson.objects.filter(~Q(user_permissions = perm)) #salesperson
reviews = Review.objects.all() #review
reviews_data = pandas.read_csv('reviews.csv')
products = Product.objects.all()

for review in reviews:
    prod = review.product
    cust = review.customer
    sp = random.choice(salespersons)
    timestamp = reviews_data[
        reviews_data['EMAIL'] == cust.email
    ].iloc[0]['unixReviewTime']
    # print(timestamp)
    all_prods = random.sample(list(products), k = random.randint(1,5))
    all_prods.append(prod)

    

    transaction = Transaction(
        customer = cust,
        salesperson = sp,
        date_ordered = datetime.datetime.fromtimestamp(timestamp),
        status = 'Delivered',
        # total_price = prod.price,
        shipping_address = cust.street_address,
        city = cust.city,
        state = cust.state,
        zipcode = cust.zip_code
    )
    transaction.save()
    # print(transaction.salesperson.store)
    # print(prod)
    total = 0
    for prods in all_prods:
        qty = random.randint(1,3)
        prc = prod.price * qty
        transaction_item = TransactionItem(
            transaction = transaction,
            inventory = Inventory.objects.get(store = transaction.salesperson.store, product = prod),
            quantity = qty,
            price = prc
        )
        total += prc
        transaction_item.save()
    
    transaction.total_price = total
    transaction.save()

    

