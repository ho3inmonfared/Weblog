from django.shortcuts import render
from . import models


def post_list_view(request):
    
    posts=models.Post.objects.filter(status='pub').order_by('-created_at')
    
    context={
        'post_list':posts
    }
    
    return render(request,'blog/post_list.html',context)
    
