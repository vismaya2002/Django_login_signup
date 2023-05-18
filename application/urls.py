from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('signup/',signup),
    path('login/',loginuser),
    path('logout/',logoutuser)
]