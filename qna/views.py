from django.http import JsonResponse
from .models import Page, Question

def get_pages(request):
    pages_data = []

    # Get all pages
    pages = Page.objects.all()

    for page in pages:
        questions_data = []

        # Get all questions for the page
        questions = page.questions.all()

        for question in questions:
            # Get the answer options for the question
            answer_options = question.get_answer_options()
            answers_data = [{"text": option.text, "value": option.value} for option in answer_options]

            questions_data.append({
                "question_text": question.question_text,
                "question_type": question.question_type.type_name,
                "answers": answers_data
            })

        pages_data.append({
            "questions": questions_data
        })

    return JsonResponse({"pages": pages_data})
