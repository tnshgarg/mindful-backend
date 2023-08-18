from rest_framework import serializers
from .models import QuestionType, Question, AnswerOption, Page, Intake

class AnswerOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerOption
        fields = ('text', 'value')

class QuestionSerializer(serializers.ModelSerializer):
    answer_options = AnswerOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('question_type', 'question_text', 'answer_options')

class PageSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Page
        fields = ('questions',)

class IntakeSerializer(serializers.ModelSerializer):
    pages = PageSerializer(many=True)

    class Meta:
        model = Intake
        fields = ('name', 'pages')

class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionType
        fields = ('type_name',)
