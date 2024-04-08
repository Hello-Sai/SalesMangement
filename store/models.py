from collections.abc import Iterable
from django.db import models

from accounts.models import Employee

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    employees = models.ManyToManyField(Employee,related_name="products")
    sales = models.BigIntegerField(default=0)
    # customers = models.ManyToManyField(Customer,related_name="products")

    def __str__(self) -> str:
        return f'{self.name} - {self.price}  '
    
    # def saleBy(self,employee):
    #     self.sales+=1
    #     self.employees.get(id = employee.id).sales+=1