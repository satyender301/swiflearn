

from django.urls import path
from.import views


urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('learn',views.learn,name='learn'),
    path('logout',views.logout,name='logout'),
   
   
]
