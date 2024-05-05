from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import DetailView
from .models import BugReport, FeatureRequest


def index(request):
    b_list = reverse('q_control:bug_list')
    f_list = reverse('q_control:feature_list')
    html = (f"<h1>Система контроля качества</h1> "
            f"<p><a href='{b_list}'>Список всех багов</a></p> "
            f"<p><a href='{f_list}'>Запросы на улучшение</a></p>")
    return HttpResponse(html)


def bug_list(request):
    bugs = BugReport.objects.all()
    bugs_html = f"<h1>Cписок отчетов об ошибках</h1><ul>"
    for bug in bugs:
        bugs_html += f'<li><a href="{bug.id}/">{bug.title} - {bug.status}</a></li>'
    bugs_html += '</ul>'
            
    return HttpResponse(bugs_html)


def feature_list(request):
    feature = FeatureRequest.objects.all()
    feature_html = f"<h1>Список запросов на улучшение</h1>"
    for featch in feature:
        feature_html += f'<li><a href="{featch.id}">{featch.title} - {featch.status}</a></li>'
    return HttpResponse(feature_html)


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        bug = self.get_object()
        project = bug.project
        task = bug.task
        
        project_url = reverse('tasks:project_detail', kwargs={'project_id': project.id})
        task_url = reverse('tasks:task_detail', kwargs={'project_id': project.id,'task_id': task.id})

        response_html = (f'<h1>{bug.title}</h1>'
            f'<h3>Статус: {bug.status}</h3>'
            f'<h3>Приоритет: {bug.priority}</h3>'
            f'<h3>Описание:</h3>' 
            f'<ul>{bug.description}</ul>'
            f'<h3>Проект:</h3>'
            f'<ul><a href="{project_url}">{project.name}</a></ul>'
            f'<h3>Задача:</h3>'
            f'<ul><a href="{task_url}">{task.name}</a></ul>')
            
        return HttpResponse(response_html)


class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        feature = self.get_object()
        project = feature.project
        task = feature.task

        project_url = reverse('tasks:project_detail', kwargs={'project_id': project.id})
        task_url = reverse('tasks:task_detail', kwargs={'project_id': project.id,'task_id': task.id})
        
        response_html = (f'<h1>{feature.title}</h1>'
            f'<h3>Статус: {feature.status}</h3>'
            f'<h3>Приоритет: {feature.priority}</h3>'
            f'<h3>Описание:</h3>' 
            f'<ul>{feature.description}</ul>'
            f'<h3>Проект:</h3>'
            f'<ul><a href="{project_url}">{project.name}</a></ul>'
            f'<h3>Задача:</h3>'
            f'<ul><a href="{task_url}">{task.name}</a></ul>')

        return HttpResponse(response_html)
