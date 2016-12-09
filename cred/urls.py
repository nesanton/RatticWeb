from django.conf.urls import url
from django.conf import settings
from cred import views as cred_views

urlpatterns = [
    # New list views
    url(r'^list/$', cred_views.list, name='list'),
    url(r'^list-by-(?P<cfilter>\w+)/(?P<value>[^/]*)/$', cred_views.list, name='list'),
    url(r'^list-by-(?P<cfilter>\w+)/(?P<value>[^/]*)/sort-(?P<sortdir>ascending|descending)-by-(?P<sort>\w+)/$', cred_views.list, name='list'),
    url(r'^list-by-(?P<cfilter>\w+)/(?P<value>[^/]*)/sort-(?P<sortdir>ascending|descending)-by-(?P<sort>\w+)/page-(?P<page>\d+)/$', cred_views.list, name='list'),

    # Search dialog for mobile
    url(r'^search/$', cred_views.search, name='search'),

    # Single cred views
    url(r'^detail/(?P<cred_id>\d+)/$', cred_views.detail, name='detail'),
    url(r'^detail/(?P<cred_id>\d+)/fingerprint/$', cred_views.ssh_key_fingerprint, name='ssh_key_fingerprint'),
    url(r'^detail/(?P<cred_id>\d+)/download/$', cred_views.downloadattachment, name='downloadattachment'),
    url(r'^detail/(?P<cred_id>\d+)/ssh_key/$', cred_views.downloadsshkey, name='downloadsshkey'),
    url(r'^edit/(?P<cred_id>\d+)/$', cred_views.edit, name='edit'),
    url(r'^delete/(?P<cred_id>\d+)/$', cred_views.delete, name='delete'),
    url(r'^add/$', cred_views.add, name='add'),

    # Adding to the change queue
    url(r'^addtoqueue/(?P<cred_id>\d+)/$', cred_views.addtoqueue, name='addtoqueue'),

    # Bulk views (for buttons on list page)
    url(r'^addtoqueue/bulk/$', cred_views.bulkaddtoqueue, name='bulkaddtoqueue'),
    url(r'^delete/bulk/$', cred_views.bulkdelete, name='bulkdelete'),
    url(r'^undelete/bulk/$', cred_views.bulkundelete, name='bulkundelete'),
    url(r'^addtag/bulk/$', cred_views.bulktagcred, name='bulktagcred'),

    # Tags
    url(r'^tag/$', cred_views.tags, name='tags'),
    url(r'^tag/add/$', cred_views.tagadd, name='tagadd'),
    url(r'^tag/edit/(?P<tag_id>\d+)/$', cred_views.tagedit, name='tagedit'),
    url(r'^tag/delete/(?P<tag_id>\d+)/$', cred_views.tagdelete, name='tagdelete'),

    # Extras
    url(r'^tag/(?P<tag_id>\d+)/extra$', cred_views.tagextras, name='tagextras'),
    url(r'^extra/edit/(?P<extra_id>\d+)/$', cred_views.extraedit, name='extraedit'),
    url(r'^extra/delete/(?P<extra_id>\d+)/$', cred_views.extradelete, name='extradelete'),
]

if not settings.RATTIC_DISABLE_EXPORT:
    urlpatterns += [
        # Export views
        url(r'^export.kdb$', cred_views.download, name='download'),
        url(r'^export-by-(?P<cfilter>\w+)/(?P<value>[^/]*).kdb$', cred_views.download, name='download'),
    ]
