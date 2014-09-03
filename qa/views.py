from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse

from .models import Question


class HomePage(ListView):

    model = Question
    template_name = "qa/home.html"
    context_object_name = 'questions'


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
