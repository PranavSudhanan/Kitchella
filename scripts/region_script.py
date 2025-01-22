import csv
#import sys
#from django.db import models
from django.contrib.auth.models import User, Permission
from app.models import Region, Salesperson
from django.contrib.auth.hashers import make_password


def import_csv_data(filepath):
    with open (filepath, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        associate_perm = Permission.objects.get(codename="associate")
        manager_perm = Permission.objects.get(codename="manager")
        region_manager_perm = Permission.objects.get(codename="region_manager")


        for row in reader:
            region_manager_list = Salesperson.objects.filter(name = row[2])
            if len(region_manager_list) > 0:
                region_manager = region_manager_list[0]
                region_manager.user_permissions.add(manager_perm)
                region_manager.user_permissions.add(region_manager_perm)
                region_manager.kind = "Region Manager"
                region_manager.save()
            else:
                region_manager = Salesperson(
                    username = row[2].replace(" ", "_"),
                    password = make_password("a_strong_password",  hasher='default'),
                    kind = "Region Manager",
                    name = row[2],
                    street_address = "default",
                    email = "default@default.com",
                    job_title = "default",
                    salary = 12
                )
                region_manager.save()
                region_manager.user_permissions.add(associate_perm)
                region_manager.user_permissions.add(manager_perm)
                region_manager.user_permissions.add(region_manager_perm)
                region_manager.save()
                
            obj = Region(
               #region_ID = row[0],
                name = row[1],
                region_manager = region_manager)
            
            print(obj)
            
            #sys.stdout.flush()
            obj.save()
            region_manager.region = obj
            region_manager.save()
            
       
#if __name__ == '__main__':
csv_file_path = 'region.csv'
import_csv_data(csv_file_path)


