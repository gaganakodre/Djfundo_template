from django.urls import path
from personal import views

urlpatterns = [
   path('index/', views.index),
   path('register/', views.register,name='register'),
   path('login/', views.login_view,name='login'),
   path('home', views.home_view,name='home'),
     
]