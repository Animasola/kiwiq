#-*- coding:utf-8 -*-
from django.test import TestCase

from qa.models import Question


class QuestionModelTestCase(TestCase):

    fixtures = ['initial_data.json']

    def setUp(self):
        self.question = Question.objects.all()[0]
        self.max_text_length = 50
        self.greater_len = 100
        self.smaller_len = 10

    def test_get_minified_text(self):
        # case when text length < max_text_length
        self.question.text = "." * self.smaller_len
        self.question.save()
        self.assertEquals(len(self.question.text), self.smaller_len)
        expected_value = self.question.text
        self.assertEquals(
            expected_value,
            self.question.get_minified_text(max_length=self.max_text_length)
        )
        # case when text length > max_text_length
        self.question.text = "." * self.greater_len
        self.question.save()
        self.assertEquals(len(self.question.text), self.greater_len)
        expected_value = self.question.text[:self.max_text_length] + u'...'
        self.assertEquals(
            expected_value,
            self.question.get_minified_text(max_length=self.max_text_length))
