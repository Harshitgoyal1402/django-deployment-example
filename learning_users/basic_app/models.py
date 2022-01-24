from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    portfolio_site = models.URLField(blank=TRUE)
    profile_pic = models.ImageField(upload_to = 'profile_pics',blank=TRUE)


    def __str__(self):
        return self.user.username
        
