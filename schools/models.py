from django.db import models
from uuid import uuid4
# Create your models here.
class School(models.Model):
    name = models.CharField(verbose_name='Inistitution Name',max_length=100,blank=False,null=False)
    id= models.UUIDField(primary_key=True, default=uuid4, editable=False)
    county = models.CharField(max_length=100,blank=False,null=False)
    
    def __str__(self):
        return f"{self.name}" 
    
    
class Apartment(models.Model):
    name = models.CharField(verbose_name='Apartment Name',max_length=100,blank=False,null=False)
    sch = models.ForeignKey(School,on_delete=models.CASCADE,blank=True,null=True)
    description = models.CharField(max_length=500,blank=True,null=True)
    rent = models.CharField(verbose_name='Amount/Month',default='2000',max_length=100,blank=False,null=False)
    
    def __str__(self):
        return f"{self.name}" 
    
    
