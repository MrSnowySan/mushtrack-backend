from django.urls import path
from . import views

urlpatterns = [
    path('create-batch/', views.create_batch, name='create_batch'),
]
