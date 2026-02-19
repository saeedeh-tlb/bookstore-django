from django.db import models
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Book(models.Model):

    CATEGORY_CHOICES=[
        ("SC" , "Science"),
        ("FN" , "Fun"),
        ("HC" , "Historic")
    ]
    name=models.CharField(max_length=50)
    published_date=models.DateField()
    price=models.FloatField()
    category=models.CharField(max_length=2 , choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title




class BookImage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="books/")

    def __str__(self):
        return f"Image for {self.book.title}"


