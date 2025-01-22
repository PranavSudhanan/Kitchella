from app.models import Category
import os

categories = list(Category.objects.all())
categories.reverse()

for i, category in enumerate(categories):
    category.image = os.path.join(os.sep, 'media/category_images' + os.sep, f'{i+1}.jpeg')
    category.save()
