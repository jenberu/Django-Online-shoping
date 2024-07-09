from django.urls import path
from . import views
urlpatterns = [ 
 path('signupaccount/', views.signupaccount, name='signupaccount'),
 path('logout/', views.logoutaccount,name='logoutaccount'),
 path('login/', views.loginaccount, name='loginaccount'),
 path('update_profile/', views.update_profile, name='update_profile'),
path('resset_passowrd/', views.resset_password, name='resset_passowrd'),
]