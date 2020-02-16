from django.contrib import admin

from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['todotext', 'complete', ]
    list_editable = ['complete',]
