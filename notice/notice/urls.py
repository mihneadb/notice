from django.conf.urls import patterns, include, url
from django.contrib import admin

from board.views import HomePageView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'notice.views.home', name='home'),
    # url(r'^notice/', include('notice.foo.urls')),
    url(r'^$', HomePageView.as_view()),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
