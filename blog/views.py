#from django.shortcuts import render,get_object_or_404,redirect
from . import models
from . import forms
from django.views import generic
from django.urls import reverse_lazy


class PostListView(generic.ListView):
    model=models.Post
    template_name='blog/post_list.html'
    context_object_name='post_list'
    
    def get_queryset(self):
        return models.Post.objects.filter(status='pub').order_by('-created_at')

# def post_list_view(request):   
#     posts=models.Post.objects.filter(status='pub').order_by('-created_at') 
#     context={
#         'post_list':posts
#     }
#     return render(request,'blog/post_list.html',context)

class PostDetailView(generic.DetailView):
    model=models.Post
    template_name='blog/post_detail.html'
    context_object_name='post'

# def post_detail_view(request,pk):
#     post=get_object_or_404(models.Post,pk=pk)
#     context={
#         'post':post
#     }
#     return render(request,'blog/post_detail.html',context)

class NewPostListView(generic.ListView):
    model=models.Post
    template_name='blog/new_post_list.html'
    context_object_name='post_list'
    
    def get_queryset(self):
        return models.Post.objects.filter(status='pub').order_by('-created_at')[:6]

# def new_post_list_view(request):
#     posts=models.Post.objects.filter(status='pub').order_by('-created_at')[:6]
#     context={
#         'post_list':posts
#     }
#     return render(request,'blog/new_post_list.html',context)

class AboutUsView(generic.TemplateView):
    template_name='blog/about_us.html'

# def about_us_view(request):
#     return render(request,'blog/about_us.html',{})

class ContactView(generic.TemplateView):
    template_name='blog/contact.html'

# def contact_view(request):
#     return render(request,'blog/contact.html',{})

class AddNewPostView(generic.CreateView):
    model=models.Post
    form_class=forms.PostForm
    context_object_name='form'
    template_name='blog/add_new_post_page.html'

# def add_new_post_view(request):
#     if request.method == "POST":
#         form=forms.PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form=forms.PostForm()
#             return redirect('post_list_page')
#     else:
#         form=forms.PostForm()  
#     context={
#         'form':form
#     }
#     return render(request,'blog/add_new_post_page.html',context)

class PostUpdateView(generic.UpdateView):
    model=models.Post
    form_class=forms.PostForm
    template_name='blog/post_update_page.html'
    context_object_name='form'

# def post_update_view(request,pk):
#     post=get_object_or_404(models.Post,pk=pk)
#     form=forms.PostForm(request.POST or None,instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('post_list_page')
#     return render(request,'blog/post_update_page.html',{'form':form})

class PostDeleteView(generic.DeleteView):
    model=models.Post
    template_name='blog/post_delete_page.html'
    success_url=reverse_lazy('post_list_page')
    context_object_name='post'

# def post_delete_view(request,pk):
#     post=get_object_or_404(models.Post,pk=pk)  
#     if request.method == "POST":
#         post.delete()
#         return redirect('post_list_page')   
#     return render(request,'blog/post_delete_page.html',{'post':post})
