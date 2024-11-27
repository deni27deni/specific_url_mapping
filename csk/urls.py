from django.urls import path
from csk.views import *

urlpatterns=[
    path('captain/',captain,name='captain'),
    path('vicecaptain/',vicecap,name='vicecaptain')
]