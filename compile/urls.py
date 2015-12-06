from django.conf.urls import patterns,url
from compile import views

urlpatterns=patterns(
'',
url(r'^editor/',views.editor),
url(r'^compile/',views.compile),
)
