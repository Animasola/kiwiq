from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import login, logout
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('qa.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    (r'^answers/', include('django_comments.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
