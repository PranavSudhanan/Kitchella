import csv

# from django.db import models
from django.contrib.auth.models import User, Permission
from app.models import Store, Region, Salesperson
from django.contrib.auth.hashers import make_password

def import_csvdata(filepath):
    with open (filepath, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        associate_perm = Permission.objects.get(codename="associate")
        manager_perm = Permission.objects.get(codename="manager")
        i = 0
        for row in reader:

            manager = Salesperson(
                    username = "manager" + str(i),
                    password = make_password("a_strong_password",  hasher='default'),
                    kind = "Manager",
                    name = "manager name",
                    street_address = "default",
                    email = "default@default.com",
                    job_title = "default",
                    salary = 12
            )
            manager.save()
            manager.user_permissions.add(associate_perm)
            manager.user_permissions.add(manager_perm)
            manager.save()
            i = i + 1
                
            sto = Store(
                
                #store_ID = row[0],
                pk = row[5],
                address = row[1],
                manager = manager,
                #number_of_salesperson = row[3],
                region =Region.objects.get(name = row[4]))
            
            sto.save()
            manager.store = sto
            manager.save()
           
#if __name__ == '__main__':

csv_file_path = 'store.csv'
import_csvdata(csv_file_path)

   #Region() got unexpected keyword arguments: 'region'
