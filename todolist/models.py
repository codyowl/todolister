from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
	name = models.CharField(max_length=100, null=False, verbose_name=u"todoname")
	isdone = models.BooleanField(default=False, verbose_name=u"task status")
	isnew = models.BooleanField(default=True, verbose_name=u"new task")
	created_date = models.DateTimeField(auto_now_add=True, blank=True)
	
	def __unicode__(self):
		return self.name

class Todolist(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=250)
	todo = models.ForeignKey(Todo, null=True, blank=True,related_name='todos', verbose_name=u'todoList')
	isnew = models.BooleanField(default=True, verbose_name=u"new task")
	created_date = models.DateTimeField(auto_now_add=True, blank=True)

	def __unicode__(self):
		return self.title

	def get_all_todo(self):
		todos = Todo.objects.all()	