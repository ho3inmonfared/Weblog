from django.shortcuts import render

def post_list_view(request):
    return render(request,'blog/post_list.html',{})
    
