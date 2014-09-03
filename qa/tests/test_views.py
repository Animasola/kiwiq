#-*- coding:utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse

from qa.models import Question
from qa.views import QUESTIONS_PER_PAGE


class QuestionListViewTestCase(TestCase):

    fixtures = ['initial_data.json']

    def setUp(self):
        self.questions = Question.objects.all()
        self.total_questions = self.questions.count()
        self.expected_num_pages = self.total_questions / QUESTIONS_PER_PAGE
        # calculating expected number of pages
        if self.total_questions % QUESTIONS_PER_PAGE != 0:
            self.expected_num_pages = self.expected_num_pages + 1

    def test_context(self):
        # check post is not allowed
        response = self.client.post(reverse('home'))
        self.assertEquals(response.status_code, 405)
        # checking context variables
        response = self.client.get(reverse('home'))
        self.assertIn('questions', response.context)
        self.assertIn('is_paginated', response.context)
        if self.total_questions <= QUESTIONS_PER_PAGE:
            self.assertFalse(response.context['is_paginated'])
        else:
            self.assertTrue(response.context['is_paginated'])
        # checking default var name page_obj
        self.assertIn('page_obj', response.context)
        page_obj = response.context['page_obj']
        self.assertEquals(page_obj.paginator.count, self.total_questions)
        self.assertEquals(
            page_obj.paginator.num_pages,
            self.expected_num_pages
        )
