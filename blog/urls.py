from django.urls import path
from . import views


urlpatterns=[
    path('',views.post_list_view,name='post_list_page'),
    path('about_us/',views.about_us_view,name='about_us_page')
    
]