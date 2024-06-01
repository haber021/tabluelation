from django.urls import path
from . import views

app_name = 'user1'

urlpatterns = [
    path('', views.index, name='index'),
    # Add other URL patterns here
]
