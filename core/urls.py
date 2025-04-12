from django.urls import path
from . import views

urlpatterns = [
    path('create-batch/', views.create_batch, name='create_batch'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('create-batch/', views.create_batch, name='create_batch'),
    path('get-batches/', views.get_batches, name='get_batches'),  # 👈 ADD THIS
]
