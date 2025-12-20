from django.urls import path
from . import views


urlpatterns=[
    path('',views.post_list_view,name='post_list_page'),
    path('detail/<int:pk>',views.post_detail_view,name='post_detail_page'),
    path('new_post/',views.new_post_list_view,name='new_post_list_page'),
    path('about_us/',views.about_us_view,name='about_us_page'),
    path('contact/',views.contact_view,name='contact_page'),
    path('add_post/',views.add_new_post_view,name='add_new_post_page'),
    path('<int:pk>/update/',views.post_update_view,name='post_update_page'),
    path('<int:pk>/delete/',views.post_delete_view,name='post_delete_page')
    
]