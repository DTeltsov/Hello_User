from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('all_users', views.get_all_users, name='all_users'),
]


