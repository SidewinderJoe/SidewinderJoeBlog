from django.http import HttpResponse
from django.template import Template , Context
from django.shortcuts import render_to_response
from posts.models import Entry

def home(request):
    return render_to_response('home.html')
    entry = Entry.objects.all()