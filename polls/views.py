from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.http import Http404

# Create your views here.

from .models import Question
from django.template import loader

"""
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')

    context = {
        'latest_questions': latest_questions,
    }
    return HttpResponse(template.render(context, request))
    
shortcut below, using django.shortcuts.render
"""

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_questions': latest_questions}
    return render(request, 'polls/index.html', context)

"""
def detail(request, question_id):
    try:
        return HttpResponse('ur looking at question %s.' % question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'polls/detail.html', {'question': question})
shortcut below using django.shortcuts.get_object_or_404
"""




def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = 'ur looking at the results of question %s.'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('ur voting on the question %s.' % question_id)
