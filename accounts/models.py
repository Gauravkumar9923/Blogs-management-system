from django.db import models

# Create your models here.
from django.db import models
from uuid import uuid4
from accounts.helpers import ROLE_CHOICES

# Create your models here.

class Users(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=36, default=uuid4)
    password = models.CharField("password", max_length=128,default="12345")
    registration_number = models.CharField(unique=True,blank=True, max_length=100)
    first_name = models.CharField("user first name",blank=True,null=True, max_length=100)
    last_name = models.CharField("user last name",blank=True,null=True,max_length=100)
    mobile_number = models.CharField("user mobile number",unique=True,blank=True,null=True,max_length=15)
    email = models.EmailField("email address", blank=True, null=True)
    create_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=6,choices=ROLE_CHOICES,default='reader')

    @classmethod
    def register_user(cls,**kwargs):
        obj = cls(**kwargs)
        obj.save()
        return obj

class UserLogin(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=36, default=uuid4)
    account = models.ForeignKey(Users,on_delete=models.CASCADE)
    login_created_timestamp = models.DateTimeField(auto_now_add=True)
    login_update_timestamp = models.DateTimeField(auto_now=True)

    @classmethod
    def user_login(cls,**kwargs):
        obj = cls(**kwargs)
        obj.save()
        return obj
