from django.db import models

class Student(models.Model):
    first_name =models.CharField(max_length=20)
    last_name =models.CharField(max_length=20)
    contact = models.IntegerField()
    email = models.EmailField(max_length=50)
    age =models.IntegerField

    def __str__(self):
        return self.first_name


     


# Create your models here.
