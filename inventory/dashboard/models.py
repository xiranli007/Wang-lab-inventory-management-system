from django.db import models
from django.contrib.auth.models import User

class Inventory(models.Model):
    name = models.CharField(max_length=300, null=True)
    catelogNumber = models.CharField(max_length=50, null=True)
    quantity = models.PositiveBigIntegerField(null=True)
    vendor = models.CharField(max_length= 100, null = True)
    receivedBy = models.CharField(max_length=100, null= True)
    storage = models.TextField(null = True) 
    receivedDate = models.DateTimeField(auto_now=True, null = True)
    
    def __str__(self):
        return f'{self.name}'

class Order(models.Model):
    name = models.CharField(max_length=300, null=True)
    staff = models.CharField(max_length= 30, null=True)
    catelogNumber = models.CharField(max_length=50, null=True)
    quantity = models.PositiveBigIntegerField(null=True)
    vendor = models.CharField(max_length= 100, null = True)
    orderedDate = models.DateTimeField(auto_now_add=True, null = True,)
    
    def __str__(self):
        return f'{self.name}'

class Request(models.Model):
    name = models.CharField(max_length=300, null=True)
    quantity = models.PositiveBigIntegerField(null=True)
    catelogNumber = models.CharField(max_length=100, null=True)
    personRequest = models.CharField(max_length=30, null=True)
    link = models.URLField(max_length=200, null=True)
    vendor = models.CharField(max_length= 100, null = True)

    def __str__(self):
        return f'{self.name}'
    
class Culture(models.Model):
    boxNumber = models. CharField(max_length=30, null = True)
    organism = models.CharField(max_length=100, null=True)
    idNumber = models.CharField(max_length=100, null = True)
    copySaved = models.PositiveBigIntegerField(null=True)
    description = models.CharField(max_length=200, null = True)
    isolationSource = models.CharField(max_length=300,null=True)
    alternateDesignation = models.CharField(max_length=300, null=True)
    receivedFrom = models.CharField(max_length=300, null=True)
    ReceivedDate = models.DateField(null=True)
    originallyReceivedFrom = models.CharField(max_length=300, null=True)
    additionalInfo = models.TextField(null=True)

    def __str__(self):
        return f'{self.organism}'
    


