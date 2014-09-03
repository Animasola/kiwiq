from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=75)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return "%s: %s" % (self.author.username, self.title)

    def get_minified_text(self, max_length=100):
        if len(self.text) <= max_length:
            result = self.text
        else:
            result = self.text[:max_length] + u'...'
        return result
