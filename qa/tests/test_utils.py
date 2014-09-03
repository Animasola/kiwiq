#-*- coding:utf-8 -*-
from django.core import mail
from django.test import TestCase

from django_comments.models import Comment

from qa.models import Question
from qa.utils import notify


class SendCommentNotificationTestCase(TestCase):

    fixtures = ['initial_data.json']

    def setUp(self):
        self.comment = Comment.objects.all()[0]
        self.question = Question.objects.get(id=self.comment.object_pk)
        self.expected_subject = "Someone answered your question"

    def test_exception(self):
        self.assertEquals(len(mail.outbox), 0)
        self.assertRaises(Exception, notify, None, None)
        self.assertRaises(Exception, notify, self.question, None)
        self.assertRaises(Exception, notify, None, self.comment)
        self.assertEquals(len(mail.outbox), 0)

    def test_with_proper_args(self):
        self.assertEquals(len(mail.outbox), 0)
        notify(self.question, self.comment)
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, self.expected_subject)
        message = mail.outbox[0].message().as_string()
        self.assertTrue(self.question.author.username.capitalize() in message)
        self.assertTrue(self.question.author.email in message)
        self.assertTrue(self.comment.user.username.capitalize() in message)
        self.assertTrue(self.comment.user.email in message)
