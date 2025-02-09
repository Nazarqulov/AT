from django.shortcuts import render

from .models import Muallim


def index(request):
    muallim=Muallim.objects.all()
    context = {'muallim':muallim}

    return render(request, 'index.html', context)
def about(request):
    return render(request, 'about.html')


# Create your views here.
