from django.urls import path
from quality_control import views

app_name = 'q_control'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('projects/', views.projects_list, name='projects_list'),
    # path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    # path('projects/<int:project_id>/tasks/<int:task_id>/', views.task_detail, name='task_detail'),

    path('', views.index, name='index'),
    path('bugs/', views.bug_list, name='bug_list'),
    path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    path('features/', views.feature_list, name='feature_list'),
    path('features/<int:feature_id>/', views.feature_id_detail, name='feature_detail'),    
]

