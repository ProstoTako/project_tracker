from django.urls import path
from quality_control import views


app_name = 'q_control'


urlpatterns = [
    path('', views.index, name='index'),
    path('bugs/', views.bug_list, name='bug_list'),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    path('bugs/new/', views.create_bug_report, name='create_bug_report'),

    path('features/', views.feature_list, name='feature_list'),
    path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
    path('features/new/', views.create_feature_request, name='create_feature_request'),
]
