from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Category, Test, Question, Answer
from .utils import *


class CategoriesView(ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = "quiz/index.html"


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        # context["test_list"] = Test.objects.all()
        return context

    slug_field = "url"


class TestDetailView(DetailView):
    model = Test

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context

    slug_field = "url"


def test_result(request, slug, next_slug):
    data = request.GET.dict()
    # print(data)
    questions = Question.objects.all()
    question_texts = [question.text for question in questions]

    current_url = request.path
    # print(current_url.split("/"))
    current_test = Test.objects.get(url=current_url.split("/")[2])

    question_counter = current_test.question_set.count()
    right_answers_counter = 0
    for key in data:
        if key in question_texts:
            current_question = questions.get(text=key)
            if data[key] == current_question.get_right_answer()[0].text:
                right_answers_counter += 1

    result = right_answers_counter / question_counter

    context = {
        "category_list": Category.objects.all(),
        "result": result
    }

    save_result_in_file(result)

    return render(request, "quiz/test_result.html", context=context)
