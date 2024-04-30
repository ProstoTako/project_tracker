from django.contrib import admin
from .models import BugReport, FeatureRequest


@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('project', 'task', 'created_at', 'updated_at', 'status', 'priority')
    list_filter = ('project', 'task', 'status', 'priority')
    search_fields = ('title', 'description')
    list_editable = ('status', 'priority')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('created_at',)
    date_hierarchy = 'created_at'

    


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('project', 'task', 'created_at', 'updated_at', 'status', 'priority')
    list_filter = ('project', 'task', 'status', 'priority')
    search_fields = ('title', 'description')
    list_editable = ('status', 'priority')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('created_at',)
    date_hierarchy = 'created_at'
