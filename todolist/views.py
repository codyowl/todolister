from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.
def todolist_home(request, template="todolist/todolist_home.html"):
	return render_to_response(template, context_instance=RequestContext(request))