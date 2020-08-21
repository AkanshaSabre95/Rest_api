from django.db import models
from django.core.validators import RegexValidator


class Companies(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    Name = models.CharField(max_length=20)
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$')
    GST = models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])

    def __str__(self):
        return self.Name


class Product(models.Model):
    Name = models.CharField(max_length=30, unique=True )
    Companies_Choices = [
        ('Lays', 'Kit-Kat', 'Perk', 'Nestle')
    ]
    Company = models.CharField(max_length=20, choices=Companies_Choices)
    Cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.Cost


class Purchase_Order(models.Model):
    Purchase_Order_Number = models.AutoField(primary_key=True, unique=True)
    Company = models.CharField(max_length=30)
    Product_Name = models.CharField(max_length=50)
    Rate = models.IntegerField(default=False)
    Quantity = models.IntegerField(default=False)
    Total_Price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.Total_Price
