import csv
# from django.db import models
from django.contrib.auth.hashers import make_password
from app.models import Salesperson, Store
from django.contrib.auth.models import User, Permission
def import_csvdata(filepath):
    with open (filepath, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        associate_perm = Permission.objects.get(codename="associate")
        manager_perm = Permission.objects.get(codename="manager")
        for row in reader:
            if row[3] != "Manager":
                kind_var = "Associate"
            else:
                kind_var = "Manager"
            sale = Salesperson(
                username = row[0].replace(" ", "_"),
                password =  make_password("a_strong_password",  hasher='default'),
                kind = kind_var,
                name = row[0],
                street_address = row[1],
                email = row[2],
                job_title = row[3],
                store= Store.objects.get(pk = row[4]),
                salary = row[5]
            )
            sale.save()
            sale.user_permissions.add(associate_perm)
            if row[3] == "Manager":
                sale.user_permissions.add(manager_perm)
            sale.save()

#if __name__ == '__main__':

csv_file_path = 'salesperson.csv'
import_csvdata(csv_file_path)
