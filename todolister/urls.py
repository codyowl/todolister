from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'todolister.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'home.views.home', name='home'),
    url(r'^signup/', 'home.views.signup', name='signup'),
    url(r'^login/', 'home.views.user_login', name='login'),
    url(r'^logout/$','django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^dashboard/', 'home.views.dashboard_home', name='dashboard_home'),
    url(r'^admin/', include(admin.site.urls)),

]

urlpatterns += patterns('',
    (r'^todolist/', include('todolist.urls')),
)

