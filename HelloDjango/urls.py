from django.conf.urls import patterns, include, url
from django.contrib import admin
from HelloDjango.views import testTemplate
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HelloDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',testTemplate),
)
