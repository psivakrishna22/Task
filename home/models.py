from django.db import models



# Create your models here.



class Signup(models.Model):



    
    name=models.CharField(max_length=255)
    dob=models.DateField()
    email=models.EmailField()
    number=models.IntegerField()
    gender=models.CharField(max_length=255)
    flatno=models.CharField(max_length=255)
    street=models.CharField(max_length=255)
    country=models.CharField(max_length=100)
    image=models.ImageField()