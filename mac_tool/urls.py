
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        url(r'^$', 'mac_tool.views.reserve'),
        url(r'^reserve', 'mac_tool.views.reserve'),
        url(r'^show', 'mac_tool.views.show'),
        )
