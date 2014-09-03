#-*- coding:utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

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


class CreateQuestionViewTestCase(TestCase):

    fixtures = ['initial_data.json']

    def setUp(self):
        Question.objects.all().delete()
        self.questions = Question.objects.all()
        self.current_user = {
            'instance': User.objects.get(username='admin'),
            'username': 'admin',
            'password': 'admin'
        }
        self.dummy_question = {
            'title': "Why the sky is blue?",
            'text': "Why the sky is blue, guys?"
        }

    def test_authorization(self):
        expected_redirect = "{0}?next={1}".format(
            reverse('auth_login'), reverse('create_question'))
        response = self.client.get(reverse('create_question'))
        self.assertRedirects(
            response,
            expected_redirect,
            status_code=302,
            target_status_code=200,
            msg_prefix=''
        )

    def test_get(self):
        self.client.login(
            username=self.current_user['username'],
            password=self.current_user['password']
        )
        response = self.client.get(reverse('create_question'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(
            response, 'name="title" type="text"', status_code=200)
        self.assertContains(
            response, 'name="text" rows="10"', status_code=200)
        self.assertContains(
            response,
            'name="post" value="Post New Question"',
            status_code=200
        )

    def test_post(self):
        self.client.login(username='admin', password='admin')
        self.assertEquals(self.questions.count(), 0)
        response = self.client.post(
            reverse('create_question'), self.dummy_question)
        # check if redirecting
        expected_redirect = reverse('home')
        self.assertRedirects(
            response,
            expected_redirect,
            status_code=302,
            target_status_code=200,
            msg_prefix=''
        )
        # check new instance
        self.assertEquals(Question.objects.all().count(), 1)
        new_question = Question.objects.all()[0]
        self.assertEquals(new_question.title, self.dummy_question['title'])
        self.assertEquals(new_question.text, self.dummy_question['text'])
        self.assertEquals(new_question.author, self.current_user['instance'])
        self.assertTrue(new_question.timestamp is not None)
