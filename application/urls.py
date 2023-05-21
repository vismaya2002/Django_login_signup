from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('signup/',signup),
    path('login/',loginuser,name='login'),
    path('logout/',logoutuser),
    path('details/',details,name='details'),
    path('display/',display,name='display'),
    path('forgot/',forgot,name='forgot')
    
]