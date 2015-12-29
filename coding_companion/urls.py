from django.conf.urls import patterns, include, url
from django.contrib import admin
from ccr import urls as ccr_urls
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'coding_companion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^ccr/',include(ccr_urls)),
    url(r'^admin/', include(admin.site.urls)),
)
