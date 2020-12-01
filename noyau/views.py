from django.shortcuts import render
from django.http import HttpResponse
from .models import Netfeelex
# Create your views here.


def homepage(request):
    return render(request = request, template_name = 'main/home.html',
                  context={"netfeelex": Netfeelex.objects.all})
