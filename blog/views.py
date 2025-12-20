from django.shortcuts import render,get_object_or_404,redirect
from . import models
from . import forms


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

def new_post_list_view(request):
    
    posts=models.Post.objects.filter(status='pub').order_by('-created_at')[:6]
    context={
        'post_list':posts
    }
    return render(request,'blog/new_post_list.html',context)

def about_us_view(request):
    
    return render(request,'blog/about_us.html',{})

def contact_view(request):
    
    return render(request,'blog/contact.html',{})
    
def add_new_post_view(request):
    
    if request.method == "POST":
        form=forms.PostForm(request.POST)
        if form.is_valid():
            form.save()
            form=forms.PostForm()
            return redirect('post_list_page')
    else:
        form=forms.PostForm()
        
    context={
        'form':form
    }
    return render(request,'blog/add_new_post_page.html',context)

def post_update_view(request,pk):
    post=get_object_or_404(models.Post,pk=pk)
    form=forms.PostForm(request.POST or None,instance=post)
    
    if form.is_valid():
        form.save()
        return redirect('post_list_page')
    
    return render(request,'blog/post_update_page.html',{'form':form})

def post_delete_view(request,pk):
    post=get_object_or_404(models.Post,pk=pk)
    
    if request.method == "POST":
        post.delete()
        return redirect('post_list_page')
    
    return render(request,'blog/post_delete_page.html',{'post':post})
