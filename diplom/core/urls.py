from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('about', views.about, name='about'),
    path('new_application', views.about, name='new_appl'),

]
