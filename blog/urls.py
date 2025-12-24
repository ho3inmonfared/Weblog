from django.urls import path
from . import views


urlpatterns=[
    path('',views.PostListView.as_view(),name='post_list_page'),
    path('detail/<int:pk>',views.PostDetailView.as_view(),name='post_detail_page'),
    path('new_post/',views.NewPostListView.as_view(),name='new_post_list_page'),
    path('about_us/',views.AboutUsView.as_view(),name='about_us_page'),
    path('contact/',views.ContactView.as_view(),name='contact_page'),
    path('add_post/',views.AddNewPostView.as_view(),name='add_new_post_page'),
    path('<int:pk>/update/',views.PostUpdateView.as_view(),name='post_update_page'),
    path('<int:pk>/delete/',views.PostDeleteView.as_view(),name='post_delete_page'),
    
]