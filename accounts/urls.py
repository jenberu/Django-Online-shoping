from django.urls import path
from . import views
from django.views.i18n import JavaScriptCatalog
urlpatterns = [ 
 path('signupaccount/', views.signupaccount, name='signupaccount'),
 path('logout/', views.logoutaccount,name='logoutaccount'),
 path('login/', views.loginaccount, name='loginaccount'),
 path('update_profile/', views.update_profile, name='update_profile'),
path('resset_passowrd/', views.resset_password, name='resset_passowrd'),
path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),

]