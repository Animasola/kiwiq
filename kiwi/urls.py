from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('qa.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^answers/', include('django_comments.urls')),
    url(r'^password/change/$',
                    'django.contrib.auth.views.password_change',
                    name='password_change'),
    url(r'^password/change/done/$',
                    'django.contrib.auth.views.password_change_done',
                    name='password_change_done'),
    url(r'^password/reset/$',
                    'django.contrib.auth.views.password_reset',
                    name='password_reset'),
    url(r'^accounts/password/reset/done/$',
                    'django.contrib.auth.views.password_reset_done',
                    name='password_reset_done'),
    url(r'^password/reset/complete/$',
                    'django.contrib.auth.views.password_reset_complete',
                    name='password_reset_complete'),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
                    'django.contrib.auth.views.password_reset_confirm',
                    name='password_reset_confirm'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
