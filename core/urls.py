from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('experience/', views.experience, name='experience'),
    path('projects/', views.projects, name='projects'),
    path('project/<int:id>/', views.project_detail, name='project_detail'),
    path('skills/', views.skills, name='skills'),
    path('cv/', views.download_cv, name='download_cv'),

]