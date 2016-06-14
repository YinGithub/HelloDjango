from django.conf.urls import patterns, include, url
from django.contrib import admin
from HelloDjango import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HelloDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',views.testMeta),
    url(r'^getCard$',views.getCard),
    url(r'^cardList$',views.cardList),
)

urlpatterns = [
    url(r'^$',views.testMeta),
    url(r'^getCard$',views.getCard),
    url(r'^cardList$',views.cardList),
]
