from django.urls import path
from . import views

app_name = 'johnny'
urlpatterns = [
    path('', views.index, name='index')
]
