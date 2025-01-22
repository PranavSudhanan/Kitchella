import pandas 
from app.models import Product, Category, Review, Customer
import os

electronics = pandas.read_csv('electronics.csv')
reviews = pandas.read_csv('reviews.csv')

for row in electronics.itertuples():
    
    prod = Product(
        name = row.title,
        price = row.price,
        # stock = 10,
        category = Category.objects.get(pk = row.category_id),
        image = os.path.join('product_images/', row.imgUrl.split('/')[-1])
    )
    prod.save()
    subset = reviews[reviews["asin"] == row.asin]
    
    for row2 in subset.itertuples():
        cust = Customer.objects.get(email = row2.EMAIL)
        rev = Review(
        customer = cust,
        product = prod,
        rating = int(row2.overall),
        comment = row2.reviewText
        )
        rev.save()