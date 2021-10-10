from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField()
    author = models.CharField(max_length=200, default='anonymous')
    email = models.EmailField(blank=True)
    describe = models.TextField(default='Library database CRUD using Django')

    def __str__(self):
        return self.name