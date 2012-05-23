from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^/index/$', 'bookmark.views.index', name='bookmark_list'),
    url(r'^/create/$', 'bookmark.views.create', name='bookmark_create'),
    url(r'^/update/(?P<bookmark_id>\d+)/$', 'bookmark.views.update', name='bookmark_update'),
    url(r'^/delete/(?P<bookmark_id>\d+)/$', 'bookmark.views.delete', name='bookmark_delete'),
    url(r'^/show/(?P<bookmark_id>\d+)/$', 'bookmark.views.show', name='bookmark_show'),
)
