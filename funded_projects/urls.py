from django.urls import path
from . import views

app_name = 'funded_projects'

urlpatterns = [
    path('', views.project_list, name='project_list'),
]