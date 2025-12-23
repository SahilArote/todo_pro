from django.contrib import admin
from .models import Todo
from simple_history.admin import SimpleHistoryAdmin


@admin.register(Todo)
class TodoAdmin(SimpleHistoryAdmin):
	list_display = ('title', 'owner', 'completed', 'created_at')
	list_filter = ('completed', 'owner')
	search_fields = ('title', 'description')
