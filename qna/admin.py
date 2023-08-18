from django.contrib import admin

# Register your models here.
from .models import QuestionType, Question, AnswerOption, Page, Intake

class AnswerOptionInline(admin.StackedInline):
    model = AnswerOption
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerOptionInline]

admin.site.register(QuestionType)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Page)
admin.site.register(Intake)
