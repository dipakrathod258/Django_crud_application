from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    alternate_email = models.CharField(max_length=30)
    mobile = models.CharField(max_length=15)
    alternate_mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=60)
    hobbies = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)