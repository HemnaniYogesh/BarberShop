from django.db import models


# Create your models here.
class Inquiry(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField()
    barber1 = models.CharField(max_length=20)
    t_date = models.CharField(max_length=10)
    t_time = models.CharField(max_length=10)
    comment = models.CharField(max_length=50)

    def __str__(self):
        return self.date, self.time


class Form(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    purpose = models.CharField(max_length=50)

class Blog(models.Model):
    img = models.ImageField(upload_to='image/')
    description = models.CharField(max_length=100)

class Portfolio(models.Model):
    img = models.ImageField(upload_to='image/')

class About(models.Model):
    img = models.ImageField(upload_to='image/')
    detail = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)

class Hairstyle(models.Model):
    hairstyle = models.CharField(max_length=20)
    price = models.CharField(max_length=10)

class Massage(models.Model):
    massage = models.CharField(max_length=20)
    price = models.CharField(max_length=10)

class Beardstyle(models.Model):
    beardstyle = models.CharField(max_length=20)
    price = models.CharField(max_length=10)