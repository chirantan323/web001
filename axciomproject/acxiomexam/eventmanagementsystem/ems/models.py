from django.db import models
from django.forms import ModelForm

#<.............ADMIN..............>#
class admin1(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Meta:
    db_table="admin1"


class user(models.Model):
    name=models.CharField(max_length=100)
    userid=models.CharField(max_length=20)
    phno=models.CharField(max_length=12,default="")
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Meta:
    db_table="user"

#<.............VENDOR..............>#
class vendor(models.Model):
    name=models.CharField(max_length=100)
    userid=models.CharField(max_length=20)
    phno=models.CharField(max_length=12,default="")
    category=models.CharField(max_length=20,default="")
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Meta:
    db_table="vendor"

# Create your models here.
