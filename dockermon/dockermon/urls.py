from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dockermon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   url(r'^$', 'dockermon.views.home', name='home'),
   url('', include('social.apps.django_app.urls', namespace='social')),
   url('', include('django.contrib.auth.urls', namespace='auth')),
   url(r'^admin/', include(admin.site.urls)),
   url(r'^latest_tweet/', 'dockermon.views.latest_tweet', name='latest_tweet'),
   url(r'^search_tweet/', 'dockermon.views.search_tweet', name='search_tweet'),
   url(r'^search/$', 'dockermon.views.search', name='search'),
   url(r'^fb/', 'dockermon.views.fb', name='fb'),
   url(r'^myloc/', 'dockermon.views.myloc', name='myloc'),
   url(r'^cal/', 'dockermon.views.cal', name='cal'),
   url(r'^whthr/', 'dockermon.views.whthr', name='whthr'),
   url(r'^main/', 'dockermon.views.main', name='main'),
   url(r'^geocode/', 'dockermon.views.geocode', name='geocode'),
   

)
