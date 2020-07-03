from django.shortcuts import render, HttpResponse
from .models import question
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    questions = question.objects.all()

    return render(request, 'question_list.html',
                  {'questions': questions, 'message': 'file format not supported, click here to download'})
