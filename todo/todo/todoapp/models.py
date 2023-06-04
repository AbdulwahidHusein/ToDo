from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    deadline = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    complated = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    
