from django.db import models
from tasks.models import Task, Project


class BugReport(models.Model):
    STATUS_CHOICES = [
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
    ]
    PRIORITY_CHOICES = [(num, str(num)) for num in range(1,6)]

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    # project = Task.objects.get(id=task.primary_key).project

    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=1,
    )

    # class Meta:
    #     constraints = [
    #         models.CheckConstraint(check=, name=''),
    #     ]

    def __str__(self):
        return str(self.title)


class FeatureRequest(models.Model):
    STATUS_CHOICES = [
        ('In_progress', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено'),
    ]
    PRIORITY_CHOICES = [(num, str(num)) for num in range(1,6)]

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    # project = Task.objects.get(id=task.primary_key).project

    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='In_progress',
    )
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=1,
    )

    def __str__(self):
        return str(self.title)
