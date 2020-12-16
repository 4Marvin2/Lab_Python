from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Processor
from .models import Description


def index(request):
    processors_list = Processor.objects.all()
    context = {'processors_list': processors_list}
    return render(request, 'catalog/index.html', context)


def detail(request, processor_id):
    processors_list = Processor.objects.all()
    for i in processors_list:
        if i.id == processor_id:
            processor = i
    description = get_object_or_404(Description, pk=processor_id)
    return render(request, 'catalog/detail.html', {'processor': processor, 'description': description})
