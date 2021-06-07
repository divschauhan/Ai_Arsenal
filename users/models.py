from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    DOB = models.DateField()
    gender = (('M',"MALE"),
              ('F',"FEMALE"))
    gender = models.CharField(max_length=10,choices=gender)
    phone = models.CharField(max_length=15)
    add = models.TextField(max_length=80,default="user address")
    city = models.CharField(max_length=20,default="not available")
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user
    





  



