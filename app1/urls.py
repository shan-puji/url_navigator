from django.urls import path
from app1.views import *
app_name='Puji'
urlpatterns=[
    path('sample1/',sample1,name='sample1')
]