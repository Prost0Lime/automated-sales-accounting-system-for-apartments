from django.urls import path
from . import  views


urlpatterns = [
    path('', views.tests),
    path('about',views.about),

]
