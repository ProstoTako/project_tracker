from django.shortcuts import render
from django.views.generic import DetailView
from .models import BugReport, FeatureRequest


def index(request):
    return render(request, 'quality_control/index.html')


def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bugs_list': bugs})


def feature_list(request):
    feature = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'features': feature})


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'


class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_detail.html'
