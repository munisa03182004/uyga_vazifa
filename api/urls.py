from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.get_notes)  # localhost:8000/api/notes/
]
