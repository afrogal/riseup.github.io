from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum

# Create your models here.

INCOMETYPE_CHOICES =[
    ("Daily","Daily"),
    ("Weekly","Weekly"),
    ("Monthly","Monthly")
]
"""
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    incomes = models.CharField(max_length = 10, choices=INCOMETYPE_CHOICES)
    Savings = models.IntegerField( null=True, blank=True)
    income = models.BigIntegerField(null=True, blank=True)
    #image = models.ImageField(upload_to='profile_image',blank=True)
    def __str__(self):
       return self.user.username
"""