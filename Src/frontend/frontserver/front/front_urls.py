__author__ = 'zdvitas'
from django.conf.urls import patterns, url


urlpatterns = patterns('',

    url(r'^$', 'front.views_front.home', name='home'),
    url(r'^login/', 'front.views_front.login'),

)
