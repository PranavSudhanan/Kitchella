#Index(['reviewerName', 'reviewerID', 'LON', 'LAT', 'NUMBER', 'STREET', 'UNIT',
    #    'CITY', 'DISTRICT', 'REGION', 'POSTCODE', 'ID', 'HASH', 'STATE',
    #    'PHONE', 'ISBUSINESS', 'BUSINESS_CATEGORIES', 'MARITAL_STATUS',
    #    'ISFEMALE', 'AGE', 'EMAIL'],
    #   dtype='object')
from django.contrib.auth.hashers import make_password
import pandas
from app.models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
customers = pandas.read_csv('users.csv')

for i,row in enumerate(customers.itertuples()):
    # if i > 20:
    #     break
    # user = User.objects.create_user(username = str(row.reviewerName).replace(' ', '_'),
                                        # email = row.EMAIL,
                                        # password = 'password')
    custom = Customer.objects.filter(username = row.reviewerName)
    if len(custom) > 0:
        username = row.reviewerName + str(i)
    else:
        username =row.reviewerName
    cust = Customer(
        # user = user,
        # reviewer_id = row.reviewerID,
        username = username,
        name = row.reviewerName,
        email = row.EMAIL,
        password = make_password("a_strong_password",  hasher='default'),
        phone_number = row.PHONE,
        street_address = str(row.NUMBER) + str(row.STREET),
        city = row.CITY,
        state = row.STATE,
        zip_code = row.POSTCODE,
        kind = 'business' if row.ISBUSINESS == True else 'home',
        
    )
    if row.ISBUSINESS == True:
        cust.business_category = row.BUSINESS_CATEGORIES
        cust.annual_income = 10000
    else:
        cust.marital_status = 'Married' if row.MARITAL_STATUS else 'Single'
        cust.gender = 'Female' if row.ISFEMALE == False else 'Male'
        cust.age = row.AGE
    cust.save()