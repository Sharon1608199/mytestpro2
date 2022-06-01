from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home,name='hello'),
    path('link1/', views.link1,name='hello1'),
    path('link2/', views.link2, name='hello2'),
    path('link3/', views.link3, name='hello3'),
    path('link4/',views.link4, name='hello4' )
]