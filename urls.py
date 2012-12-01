from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
#        url(r'^ajax/flag_status/(?P<team_id>\d)$', 'CTFGameServer.PlayerInterface.views.flag_status'),
#        url(r'^ajax/captured_flags/(?P<team_id>\d)$',
#            'CTFGameServer.PlayerInterface.views.captured_flags'),
#        url(r'^ajax/capture_flag/(?P<team_id>\d)/(?P<secure_id>.*)$',
#            'CTFGameServer.PlayerInterface.views.recordCapture'),
#        url(r'^ajax/flag_points/(?P<team_id>\d)$',
#            'CTFGameServer.PlayerInterface.views.flag_points'),
#    url(r'^$', include('PlayerInterface.urls')),
#    url(r'^login', 'django.contrib.auth.views.login'),
#    url(r'^quiz/', include('quiz.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
