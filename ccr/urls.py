from django.conf.urls import patterns,url
from ccr import views

urlpatterns=patterns(
'',
url(r'^$',views.common),
url(r'^compile/',views.compile),
url(r'^run/',views.run),
)