from django.db import models


# Create your models here.

class Todo(models.Model):
    product = models.CharField(max_length=100)
    main_image = models.ImageField(max_length=100, upload_to='image')
    right_view = models.ImageField(max_length=100, upload_to='image')
    left_view = models.ImageField(max_length=100, upload_to='image')
    price = models.IntegerField()
    stock = models.IntegerField(default=1)
    description = models.TextField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.product
