from django.http import HttpResponse
from django.template import loader
from .models import *

def index(request):
    all_tables = Person.objects.all()
    template = loader.get_template('mafia_tables/index.html')
    context = {
        'all_tables': all_tables,
    }
    return HttpResponse(template.render(context, request))

def detail(request, Person_id):
    all_obj = Person.objects.get(pk=Person_id)
    template = loader.get_template('mafia_tables/detail.html')
    context = {
        'all_obj': all_obj,
    }
    return HttpResponse(template.render(context, request))

def taskInfo(request, Person_id, Person):
    task_obj = PersonHasTasks.objects.filter(person_id = Person_id)
    template = loader.get_template('mafia_tables/taskInfo.html')
    context = {
        'task_obj': task_obj,
    }
    return HttpResponse(template.render(context, request))
