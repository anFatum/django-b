from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    my_dict = {'insert_me': 'hello world'}
    return render(request, 'hello_world_app/index.html', context=my_dict)

# Create your views here.
