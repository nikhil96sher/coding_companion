from django.conf.urls import patterns,url
from ccr import views

urlpatterns=patterns(
'',
url(r'^$',views.main),
url(r'^save/',views.save),
url(r'^share/',views.share),
url(r'^compile/',views.compile),
url(r'^run/',views.run),
)