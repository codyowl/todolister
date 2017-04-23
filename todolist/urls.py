from django.conf.urls import include, url
from django.contrib import admin
from todolist.views import todolist_home

urlpatterns = [
    # Examples:
    # url(r'^$', 'todolister.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^todolist-home/', 'todolist.views.todolist_home', name='todolist_home'),
    
]