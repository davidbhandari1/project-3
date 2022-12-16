from django.db import models

# Create your models here.
class Contact(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    subject = models.TextField(blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name
class Informations(models.Model):
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300)
    email = models.EmailField(max_length=50)
    time =  models.CharField(max_length=200)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.address1

class Service(models.Model):
    title=models.CharField(max_length=200)
    logo =models.CharField(max_length=100)
    description= models.TextField()

    def __str__(self):
        return self.title





