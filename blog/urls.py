from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'), 
    path('about/', views.about_page, name='about_page'), 
    path('contact/', views.contact_page, name='contact_page'), 
    path('dashboard/', views.dashboard_page, name='dashboard_page'), 
    path('login/', views.user_login, name='user_login'), 
    path('signup/', views.user_signup, name='user_signup'), 
    path('logout/', views.user_logout, name='user_logout'), 
    path('create_post/', views.create_post, name='create_post'), 
    path('edit_post/<int:id>', views.edit_post, name='edit_post'), 
    path('delete_post/<int:id>', views.delete_post, name='delete_post'), 
]