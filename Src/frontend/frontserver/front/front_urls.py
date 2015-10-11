__author__ = 'zdvitas'
from django.conf.urls import patterns, url


urlpatterns = patterns('',

    url(r'^$', 'front.views_front.home', name='home'),
    url(r'^login/', 'front.views_front.login'),
    url(r'^logout/', 'front.views_front.logout'),
    url(r'^auth/', 'front.views_front.auth'),
    url(r'^add_doc/', 'front.views_front.add_doc'),

)
