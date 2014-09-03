from django.conf.urls import patterns, url

from .views import HomePage, QuestionPage


urlpatterns = patterns(
    '',
    url(r'^$', HomePage.as_view(), name='home'),
    url(r'^questions/(?P<pk>\d+)/$', QuestionPage.as_view(), name='question-detailed'),
)
