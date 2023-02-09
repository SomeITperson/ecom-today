from django.contrib import admin
from todo.models import *

class TodoAdmin(admin.ModelAdmin):
    list_display = ["uuid", "created", "body", "active"]

admin.site.register(Todo, TodoAdmin)