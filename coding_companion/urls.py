from django.conf.urls import patterns, include, url
from django.contrib import admin
from compile import urls as compile_urls
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'coding_companion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^compile/',include(compile_urls)),
    url(r'^admin/', include(admin.site.urls)),
)
