from django.db import models

class QuestionType(models.Model):
    TEXT = 'Text'
    MULTIPLE_CHOICE = 'Multiple Choice'
    SINGLE_CHOICE = 'Single Choice'
    SCALE = 'Scale'
    DATE = 'Date'
    FILE_UPLOAD = 'File Upload'
    CONSENT = 'Consent'
    DROPDOWN = 'Dropdown'
    MATRIX = 'Matrix'

    QUESTION_TYPE_CHOICES = [
        (TEXT, 'Text'),
        (MULTIPLE_CHOICE, 'Multiple Choice'),
        (SINGLE_CHOICE, 'Single Choice'),
        (SCALE, 'Scale'),
        (DATE, 'Date'),
        (FILE_UPLOAD, 'File Upload'),
        (CONSENT, 'Consent'),
        (DROPDOWN, 'Dropdown'),
        (MATRIX, 'Matrix'),
    ]

    type_name = models.CharField(max_length=50, choices=QUESTION_TYPE_CHOICES)

    def __str__(self):
        return self.type_name


class Question(models.Model):
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=1000)

    def get_answer_options(self):
        return AnswerOption.objects.filter(question=self)

    def __str__(self):
        return self.question_text

class AnswerOption(models.Model):
    question = models.ForeignKey(Question, related_name='answer_options', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.text

class Page(models.Model):
    order = models.IntegerField(null=True, unique=True)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return f"Page {self.order}"


class Intake(models.Model):
    name = models.CharField(max_length=100)
    pages = models.ManyToManyField(Page)

    def __str__(self):
        return self.name
