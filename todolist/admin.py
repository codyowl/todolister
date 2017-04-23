from django.contrib import admin
from .models import Todo, Todolist

admin.site.register(Todolist)
admin.site.register(Todo)