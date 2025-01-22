import pandas 
from app.models import Review, Customer, Product

reviews = pandas.read_csv('reviews.csv')

for i,row in enumerate(reviews.itertuples()):
    # if i > 10000:
    #     break

    cust = Customer.objects.get(email = row.EMAIL)
    prod = Product.objects.get(asin = row.asin)

    rev = Review(
        customer = cust,
        product = prod,
        rating = int(row.overall),
        reviewText = row.reviewText
    )
    rev.save()
    