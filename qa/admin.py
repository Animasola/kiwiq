from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'timestamp']
    readonly_fields = ('author',)
    search_fields = ['title', 'text']


admin.site.register(Question, QuestionAdmin)
