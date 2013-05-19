from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Children.views.home', name='home'),
    # url(r'^Children/', include('Children.foo.urls')),

    url(r'^$', 'core.views.index'),
    url(r'^registration$', 'users.views.registration'),
    url(r'^organizations$', 'core.views.organization_list'),
    url(r'^anketa$', 'users.views.anketa'),
    url(r'^interests', 'core.views.interests'),
    url(r'^interests/type/(?P<type>\d+$)', 'core.views.interests'),
    url(r'^skill$', 'users.views.skill_list'),
    url(r'^skill/(?P<id>\d+$)', 'users.views.skill_list'),
    url(r'^user$', 'core.views.cabinet')
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
