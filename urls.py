from django.urls import path
from . import views

urlpatterns = [
path('', views.list_persons, name='list_persons'), # List view as homepage
path('add/', views.create_person, name='create_person'),
path('edit/<int:pk>/', views.update_person, name='update_person'),
path('delete/<int:pk>/', views.delete_person, name='delete_person'),
]