from django.http import HttpResponse
from django.template import loader
from .models import *

def index(request):
    all_tables = BusinessType.objects.all()
    template = loader.get_template('mafia_tables/index.html')
    context = {
        'all_tables': all_tables,
    }
    return HttpResponse(template.render(context, request))

def detail(request, BusinessType_id):
    all_obj = BusinessType.objects.get(pk=BusinessType_id)
    template = loader.get_template('mafia_tables/detail.html')
    context = {
        'all_obj': all_obj,
    }
    return HttpResponse(template.render(context, request))
