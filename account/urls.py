from django.conf.urls import include, url
from django.conf import settings
from django.contrib.auth import views as auth_views

from account import views as account_views
from views import profile, newapikey, deleteapikey, RatticSessionDeleteView
from views import RatticTFADisableView, RatticTFABackupTokensView
from views import RatticTFASetupView, RatticTFALoginView
from views import RatticTFAGenerateApiKey

from two_factor.views import QRGeneratorView

urlpatterns = [
    url(r'^$', profile, {}, name='profile'),
    url(r'^newapikey/$', newapikey, {}, name='newapikey'),
    url(r'^deleteapikey/(?P<key_id>\d+)/$', deleteapikey, {}, name='deleteapikey'),

    url(r'^logout/$', auth_views.logout, {
        'next_page': settings.RATTIC_ROOT_URL}, name='logout'),

    # View to kill other sessions with
    url(r'^killsession/(?P<pk>\w+)/', RatticSessionDeleteView.as_view(), name='kill_session'),

    # Two Factor Views
    url(r'^login/$', RatticTFALoginView.as_view(), name='login'),
    url(r'^generate_api_key$', RatticTFAGenerateApiKey.as_view(), name="generate_api_key"),

    url(r'^two_factor/disable/$', RatticTFADisableView.as_view(), name='tfa_disable'),
    url(r'^two_factor/backup/$', RatticTFABackupTokensView.as_view(), name='tfa_backup'),
    url(r'^two_factor/setup/$', RatticTFASetupView.as_view(), name='tfa_setup'),
    url(r'^two_factor/qr/$', QRGeneratorView.as_view(), name='tfa_qr'),
]

if settings.GOAUTH2_ENABLED:
    urlpatterns += [
        url(r'', include('social_auth.urls')),
    ]

# URLs we don't want enabled with LDAP
if not settings.LDAP_ENABLED:
    urlpatterns += [
        url(r'^reset/$', auth_views.password_reset,
            {
                'post_reset_redirect': '/account/reset/done/',
                'template_name': 'password_reset.html'
            },
            name="password_reset"
        ),

        url(r'^reset/done/$', auth_views.password_reset_done, {
            'template_name': 'password_reset_done.html'},
            name="password_reset_done"
        ),

        url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm, {
            'post_reset_redirect': '/',
            'template_name': 'password_reset_confirm.html'},
            name="password_reset_confirm"
        ),

        url(r'^changepass/$', account_views.rattic_change_password, {
            'post_change_redirect': '/account/',
            'template_name': 'account_changepass.html'}, name='password_change')
    ]

# URLs we do want enabled with LDAP
if settings.LDAP_ENABLED and settings.AUTH_LDAP_ALLOW_PASSWORD_CHANGE:
    urlpatterns += [
        url(r'^changepass/$', account_views.ldap_password_change, {}, name='password_change')
    ]
