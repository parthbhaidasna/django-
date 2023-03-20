from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User (AbstractUser):
    is_developer = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_teamleader = models.BooleanField(default=False)
    is_tester = models.BooleanField(default=False)
    age = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)

    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta():
        db_table = 'User'
    def __str__(self):
        return self.first_name