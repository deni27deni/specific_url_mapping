from django.urls import path
from mi.views import *

urlpatterns=[
    path('captain/',captain,name='captain'),
    path('vicecaptain/',vicecap,name='vicecaptain'),
]