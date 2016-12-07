from django.conf.urls import url
from django.conf import settings
from views import NewUser, UpdateUser
from staff import views as staff_views


urlpatterns = [
    # Views in views.py
    url(r'^$', staff_views.home, name='staff_home'),

    # User/Group Management
    url(r'^userdetail/(?P<uid>\d+)/$', staff_views.userdetail, name='userdetail'),
    url(r'^removetoken/(?P<uid>\d+)/$', staff_views.removetoken, name='removetoken'),
    url(r'^groupdetail/(?P<gid>\d+)/$', staff_views.groupdetail, name='groupdetail'),

    # Auditing
    url(r'^audit-by-(?P<by>\w+)/(?P<byarg>\d+)/$', staff_views.audit, name='staff_audit'),

    # Importing
    url(r'^import/keepass/$', staff_views.upload_keepass, name='upload_keepass'),
    url(r'^import/process/$', staff_views.import_overview, name='import_overview'),
    url(r'^import/process/(?P<import_id>\d+)/$', staff_views.import_process, name='import_process'),
    url(r'^import/process/(?P<import_id>\d+)/ignore/$', staff_views.import_ignore, name='import_ignore'),

    # Undeletion
    url(r'^credundelete/(?P<cred_id>\d+)/$', staff_views.credundelete, name='credundelete'),
]

# URLs we remove if using LDAP groups
if not settings.USE_LDAP_GROUPS:
    urlpatterns += [
        # Group Management
        url(r'^groupadd/$', staff_views.groupadd, name='groupadd'),
        url(r'^groupedit/(?P<gid>\d+)/$', staff_views.groupedit, name='groupedit'),
        url(r'^groupdelete/(?P<gid>\d+)/$', staff_views.groupdelete, name='groupdelete'),
        url(r'^useredit/(?P<pk>\d+)/$', UpdateUser.as_view(), name="user_edit"),
        url(r'^userdelete/(?P<uid>\d+)/$', staff_views.userdelete, name='userdelete'),
    ]

# User add is disabled only when LDAP config exists
if not settings.LDAP_ENABLED:
    urlpatterns += [
        # User Management
        url(r'^useradd/$', NewUser.as_view(), name="user_add"),
    ]
