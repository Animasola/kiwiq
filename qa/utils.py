#-*- coding:utf-8 -*-
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.conf import settings


def notify(question, comment, request):
    url = request.build_absolute_uri(
        reverse('question-detailed', args=[question.id]))
    recipient_mail = question.author.email
    recipient_name = question.author.username.capitalize()
    subject = "Someone answered your question"
    message_schema = 'Greetings, {0}\n{1}{2}{3}'
    msg_line_1 = '\nA user {0} have answered one of your questions\n'.format(
        request.user.username.capitalize())
    msg_line_2 = 'Check this out at - {0}.\n'.format(url)
    msg_line_3 = 'Best Regards from Smack Overflow!'

    message = message_schema.format(
        recipient_name,
        msg_line_1,
        msg_line_2,
        msg_line_3
    )
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [recipient_mail],
        fail_silently=False
    )