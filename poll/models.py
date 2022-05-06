from django.db import models

# Create your models here.
from django.urls import reverse


class POST(models.Model):
    username = models.CharField(max_length=100, db_index=True)
    first_name = models.CharField(max_length=100, db_index=True)
    last_name = models.CharField(max_length=500)
    phone_number = models.IntegerField(max_length=500)
    birthday = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    city = models.CharField(max_length=500);


    def get_number(self):
        return 8

    def get_let1(self):
       return 'abc'

    def get_let2(self):
        return 'abcdfg'






