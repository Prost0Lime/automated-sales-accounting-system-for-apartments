from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('about', views.about, name='about'),
    path('new_application', views.new_appl, name='new_appl'),
    path('login', views.login, name='login'),
    path('employee', views.index, name="employee"),
    path('new_application', views.create, name="new_appl"),

]
