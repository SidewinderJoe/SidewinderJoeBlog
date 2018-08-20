from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Template , Context
from django.shortcuts import render_to_response

from howtos.models import Entry


def howtos(request,slug=None):
    entries = Entry.objects.filter(publish=True).order_by('-created')[0:5]
    entry = None # entries[0]
    if entry:
        entry = Entry.objects.get(slug=slug) # <--
    return render(request, 'howtos.html', {'entry': entry, 'entries': entries })

def entry(request,slug=None):
	page = Entry.objects.get(slug=slug)
        if slug != page.slug:
            return redirect(entry, permanent=True)

        return render(request, 'article.html',{
            'entry' : entry, 'page' : page
        })