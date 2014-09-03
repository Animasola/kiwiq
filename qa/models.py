#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from django_comments.signals import comment_was_posted

from .utils import notify
from .exceptions import EmailNotificationException


class Question(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=75)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __unicode__(self):
        return "%s: %s" % (self.author.username, self.title)

    def get_minified_text(self, max_length=100):
        if len(self.text) <= max_length:
            result = self.text
        else:
            result = self.text[:max_length] + u'...'
        return result


def notify_author(sender, comment, request, **kwargs):
    question = Question.objects.get(id=comment.object_pk)

    try:
        notify(question, comment, request)
    except Exception as e:
        raise EmailNotificationException("Failed to notify author:\n%s" % str(e))


comment_was_posted.connect(notify_author, dispatch_uid='notify_author')
