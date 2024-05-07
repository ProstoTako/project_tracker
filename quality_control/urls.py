from django.urls import path
from quality_control import views


app_name = 'q_control'


urlpatterns = [
    path('', views.index, name='index'),
    path('bugs/', views.bug_list, name='bug_list'),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    path('bugs/new/', views.create_bug_report, name='create_bug_report'),
    path('bugs/<int:bug_id>/update/', views.update_bug_report, name='update_bug_report'),
    path('bugs/<int:bug_id>/delete/', views.delete_bug_report, name='delete_bug_report'),

    path('features/', views.feature_list, name='feature_list'),
    path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
    path('features/new/', views.create_feature_request, name='create_feature_request'),
    path('features/<int:feature_id>/update/', views.update_feature_request, name='update_feature_request'),
    path('features/<int:feature_id>/delete/', views.delete_feature_request, name='delete_feature_request'),
]
