import pandas
from app.models import Category

electronics_categories = pandas.read_csv('electronics_categories.csv')

for row in electronics_categories.itertuples():
    cat = Category(
        # unique_id = row.id,
        name = row.category_name
    )
    cat.save()