from django.urls import path
from . import views

urlpatterns = [
    path('get_pages/', views.get_pages, name='get_pages'),
]
