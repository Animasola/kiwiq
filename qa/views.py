#-*- coding:utf-8 -*-
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse

from datetime import datetime

from .models import Question


QUESTIONS_PER_PAGE = 5


class HomePage(ListView):

    model = Question
    template_name = "qa/home.html"
    context_object_name = 'questions'
    paginate_by = QUESTIONS_PER_PAGE


class QuestionPage(DetailView):

    queryset = Question.objects.all()
    template_name = "qa/question_detail.html"

    def get_object(self):
        self.question = super(QuestionPage, self).get_object()

        return self.question

    def get_context_data(self, **kwargs):
        context = super(QuestionPage, self).get_context_data(**kwargs)
        context['question'] = self.question
        context['next'] = reverse('question-detailed', args=[self.question.id])

        return context


class CreateQuestion(CreateView):

    model = Question
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.timestamp = datetime.now()

        return super(CreateQuestion, self).form_valid(form)

    def get_success_url(self):
            return reverse('home')
