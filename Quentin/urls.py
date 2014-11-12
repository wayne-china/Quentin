from django.conf.urls import patterns, include, url
from django.contrib import admin
from Quentin.views import Posts,blog_detail,search,archive
from django.conf import settings
from django.views.static import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', Posts, name='posts'),
    url(r'^grappelli/',include('grappelli.urls')),
    url(r'^search/$', search, name='search'),
    url(r'^archive/$', archive, name='archive'),
    url(r'^blog_detail/(?P<id>\d+)/$', blog_detail, name='blog_detail'),
    url(r'^comments/', include('django.contrib.comments.urls')),

#    url(r'^media/base.css', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += staticfiles_urlpatterns()
