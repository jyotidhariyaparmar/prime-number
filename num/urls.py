from django.urls import path
from . import views

urlpatterns = [
    path('create_view', views.create_view, name='create_view'),
    path('list_view', views.list_view, name='list_view'),
    path('', views.home, name='home'),

]
