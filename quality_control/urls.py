from django.urls import path
from quality_control import views


app_name = 'q_control'


urlpatterns = [
    path('', views.index, name='index'),
    path('bugs/', views.BugListView.as_view(), name='bug_list'),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    path('bugs/new/', views.BugCreateView.as_view(), name='create_bug_report'),
    path('bugs/<int:bug_id>/update/', views.BugUpdateView.as_view(), name='update_bug_report'),
    path('bugs/<int:bug_id>/delete/', views.BugDeleteView.as_view(), name='delete_bug_report'),

    path('features/', views.FeatureListView.as_view(), name='feature_list'),
    path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
    path('features/new/', views.FeatureCreateView.as_view(), name='create_feature_request'),
    path('features/<int:feature_id>/update/', views.FeatureUpdateView.as_view(), name='update_feature_request'),
    path('features/<int:feature_id>/delete/', views.FeatureDeleteView.as_view(), name='delete_feature_request'),
]
