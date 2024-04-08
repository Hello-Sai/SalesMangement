from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import F

# Create your models here.
class Employee(AbstractUser):
    sales = models.BigIntegerField()


    def sale(self,products):
        self.sales+=products.count()
        products.update(sales = F('sales')+1)
        self.save()

class Customer(models.Model):
    name   = models.CharField(max_length=30)
    number = models.CharField(max_length=13,null=True,blank=True)
    email  =  models.EmailField(unique=True)
    details = models.TextField()
    # products = models.ManyToManyField(Product,)


    def __str__(self) -> str:
        return f'{self.name} ({self.email})'