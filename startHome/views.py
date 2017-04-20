
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

def index(request):
    return render_to_response('startHome/page.html', context_instance=RequestContext(request))


def page(request):
    return render(request, 'startHome/page.html')

