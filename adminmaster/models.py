from django.db import models

# Create your models here.

class Profile:
    pass

class Barber(models.Model):
    uname = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=10)

class Confirmation  (models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    phone = models.IntegerField()
    barber1 = models.CharField(max_length=20)
    email = models.EmailField()
    t_date = models.CharField(max_length=10)
    t_time = models.CharField(max_length=10)
    comment = models.CharField(max_length=50)

    def __str__(self):
        return self.date, self.time


class Staff(models.Model):
    uname = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=10)