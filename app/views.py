from django.shortcuts import render
from .models import question


# Create your views here.
def index(request):
    questions = question.objects.all()
    return render(request, 'question_list.html',
                  {'questions': questions, 'message': 'file format not supported, click here to download'})
