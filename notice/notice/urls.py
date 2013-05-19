from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'notice.views.home', name='home'),
    # url(r'^notice/', include('notice.foo.urls')),
    url(r'^$', 'board.views.homepage', name='homepage'),
    url(r'^post/add$', 'board.views.post_add', name='post_add'),
    url(r'^post/edit/(?P<id>\d+)$', 'board.views.post_edit', name='post_edit'),
    url(r'^post/delete/(?P<id>\d+)$', 'board.views.post_delete', name='post_delete'),
    url(r'^post/detail/(?P<id>\d+)$', 'board.views.post_detail', name='post_detail'),


    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {
        'template_name': 'login.html',
    }, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {
        'next_page': '/',
    }, name='logout'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
