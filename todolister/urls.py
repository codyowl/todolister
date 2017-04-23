from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'todolister.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'home.views.home', name='home'),
    url(r'^signup/', 'home.views.signup', name='signup'),
    url(r'^login/', 'home.views.user_login', name='login'),
    url(r'^admin/', include(admin.site.urls)),
]