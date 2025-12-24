from django.db import models

class Book(models.Model):

    CATEGORY_CHICES=[
        ("SC" , "Science"),
        ("FN" , "Fun"),
        ("HC" , "Historic")
    ]
    name=models.CharField(max_length=50)
    published_date=models.DateField()
    price=models.FloatField()
    category=models.CharField(max_length=2 , choices=CATEGORY_CHICES)

    def serialize(self):
        return {
            "name": self.name,
            "published_date": self.published_date,
            "price": self.price,
            "category":self.category,
        }