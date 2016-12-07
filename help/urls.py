from django.conf.urls import url
from help import views as help_views

urlpatterns = [
    url(r'^$', help_views.home, name='help_home'),
    url(r'^(?P<page>[\w\-]+)/$', help_views.markdown, name='markdown'),
]
