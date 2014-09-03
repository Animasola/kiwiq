from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import HomePage, QuestionPage, CreateQuestion


urlpatterns = patterns(
    '',
    url(r'^$', HomePage.as_view(), name='home'),
    url(r'^questions/(?P<pk>\d+)/$', QuestionPage.as_view(), name='question-detailed'),
    url(r'^create_question/$', login_required(CreateQuestion.as_view()), name='create_question'),
)
