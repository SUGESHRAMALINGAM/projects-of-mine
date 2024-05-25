from django.db import models

# Create your models here.

class LessorDetails(models.Model):
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Phone_No = models.CharField(max_length=10)
    Country = models.CharField(max_length=30)
    State = models.CharField(max_length=30)
    City = models.CharField(max_length=30)
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)

class LesseeDetails(models.Model):
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Phone_No = models.CharField(max_length=10)
    Company = models.CharField(max_length=50)
    Country = models.CharField(max_length=30)
    State = models.CharField(max_length=30)
    City = models.CharField(max_length=30)
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)

class ContainerDetails(models.Model):
    Owner_id = models.IntegerField()
    Owner_Name = models.CharField(max_length=20)
    Container_Type = models.CharField(max_length=50)
    Container_Size = models.CharField(max_length=10)
    Container_Picture = models.FileField()
    Quantity = models.IntegerField()
    Container_Amount = models.FloatField()
    Status = models.BooleanField(default=False)

class LeasingDetails(models.Model):
    Lessee_id = models.IntegerField()
    Lessee_Name = models.CharField(max_length=20)
    Owner_id = models.IntegerField() 
    Owner_Name = models.CharField(max_length=20)
    Lease_Container_Type = models.CharField(max_length=50)
    Lease_Container_Size = models.CharField(max_length=10)
    Quantity = models.IntegerField()
    Lease_Date = models.DateTimeField()
    Leasing_Months = models.IntegerField()
    Lease_Amount = models.FloatField()
    Status = models.BooleanField(default=False)
