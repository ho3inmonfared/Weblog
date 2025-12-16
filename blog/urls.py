from django.urls import path
from . import views


urlpatterns=[
    path('',views.post_list_view,name='post_list_page')
    
]