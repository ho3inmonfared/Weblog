from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    
    STATUS_CHOICES=(
        ('pub','publish'),
        ('drf','draft'),
    )
    
    title=models.CharField(max_length=100)
    description=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    status=models.CharField(choices=STATUS_CHOICES,default='drf',max_length=100)
    
    

