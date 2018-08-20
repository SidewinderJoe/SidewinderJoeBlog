from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader

# Create your views here.
from django.http import HttpResponse
from django.template import Template , Context
from django.shortcuts import render_to_response

from posts.models import Entry

#def posts(request,slug=None):
    #entries = Entry.objects.all().order_by('-created')
    #if blog_id:#
    #entry = entries[0]
    #return render(request, 'posts.html', {'entry': entry, 'entries': entries })

def posts(request,slug=None):
    entries = Entry.objects.filter(publish=True).order_by('-created')[0:5]
    entry = None # entries[0]
    if entry:
        entry = Entry.objects.get(slug=slug) # <--
    return render(request, 'posts.html', {'entry': entry, 'entries': entries })

def entry(request,slug=None):
	page = Entry.objects.get(slug=slug, publish=True)
        if slug != page.slug:
            return redirect(entry, permanent=True)

        return render(request, 'article.html',{
            'entry' : entry, 'page' : page
        })