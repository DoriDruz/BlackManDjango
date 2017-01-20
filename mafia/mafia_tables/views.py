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
