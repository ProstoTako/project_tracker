from django.shortcuts import render, redirect, get_object_or_404
from .models import BugReport, FeatureRequest

from django.http import HttpResponse
from django.urls import reverse


def index(request):
    b_list = reverse('q_control:bug_list')
    f_list = reverse('q_control:feature_list')
    html = (f"<h1>Система контроля качества</h1> "
            f"<p><a href='{b_list}'>Список всех багов</a></p> "
            f"<p><a href='{f_list}'>Запросы на улучшение</a></p>")
    return HttpResponse(html)


def bug_list(request):
    # b_list = reverse('q_control:bug_list')
    # f_list = reverse('q_control:feature_list')
    bugs = BugReport.objects.all()
    bugs_html = f"<h1>Cписок отчетов об ошибках</h1><ul>"
    for bug in bugs:
        bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a></li>'
    bugs_html += '</ul>'
            
    return HttpResponse(bugs_html)


def feature_list(request):
    # b_list = reverse('q_control:bug_list')
    # f_list = reverse('q_control:feature_list')
    html = f"<h1>Список запросов на улучшение</h1>"
    return HttpResponse(html)


def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    bug_html = f"<p>Детали бага {bug.id}</p>"
    return HttpResponse(bug_html)

def feature_id_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    feature_html = f"<p>Детали улучшения {feature.id}</p>"
    return HttpResponse(feature_html)