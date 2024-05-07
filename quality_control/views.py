from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, CreateView
from .models import BugReport, FeatureRequest
from .forms import BugReportForm, FeatureRequestForm


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


def create_bug_report(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('q_control:bug_list')
    else:
        form = BugReportForm()
        
    return render(request, 'quality_control/bug_report_form.html', {'form': form})


def create_feature_request(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('q_control:feature_list')
    else:
        form = FeatureRequestForm()

    return render(request, 'quality_control/feature_request_form.html', {'form': form})


def update_bug_report(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('q_control:bug_detail', bug_id=bug.id)
    else:
        form = BugReportForm(instance=bug)
    return render(request, 'quality_control/bug_report_update.html', {'form': form, 'bug': bug})


def update_feature_request(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('q_control:feature_detail', feature_id=feature.id)
    else:
        form = FeatureRequestForm(instance=feature)
    return render(request, 'quality_control/feature_request_update.html', {'form': form, 'feature': feature})


def delete_bug_report(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    bug.delete()

    return redirect('q_control:bug_list')


def delete_feature_request(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    feature.delete()

    return redirect('q_control:feature_list')
