from django.urls import path

from . import views

app_name = 'exam'
urlpatterns = [
    path('add/', views.add_candidate, name="add_candidate")
]