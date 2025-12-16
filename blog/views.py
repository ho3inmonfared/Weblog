from django.shortcuts import render,get_object_or_404
from . import models



def post_list_view(request):
    
    posts=models.Post.objects.filter(status='pub').order_by('-created_at')
    
    context={
        'post_list':posts
    }
    return render(request,'blog/post_list.html',context)

def post_detail_view(request,pk):
    
    post=get_object_or_404(models.Post,pk=pk)
    context={
        'post':post
    }
    return render(request,'blog/post_detail.html',context)


def about_us_view(request):
    
    return render(request,'blog/about_us.html',{})
    
