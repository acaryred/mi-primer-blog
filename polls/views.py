from django.shortcuts import HttpResponse
#from django.template import loader
from django.shortcuts import render

from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    #return HttpResponse(template.render(context, request))
    
#Antes era:    
#    output = ', '.join([q.question_text for q in latest_question_list])
#    return HttpResponse(output)

    
def detail(request, question_id):
    return HttpResponse("Buscando pregunta %s. " % question_id)
    
def results(request, question_id):
    response = "Buscas el resultado de pregunta %s. "
    return HttpResponse(response % question_id)
    
def vote(request, question_id):
    return HttpResponse("Votas por pregunta %s. " % question_id)