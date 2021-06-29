from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse

from datetime import date

from .models import Entry

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def entry(request):
    admission_years = list(range(2021, 1975, -1))
    entry_dates = [date(2021, 9, day) for day in [10, 11, 12, 13]]
    context = {
        'admission_years': admission_years,
        'entry_dates': entry_dates,
    }
    return render(request, 'register/entry.html', context)

def submit(request):
    entry = Entry.objects.create(
        screen_name=request.POST['screen_name'],
        admission_year=request.POST['admission_year'],
        start_date=request.POST['start_date'],
        end_date=request.POST['end_date'],
    )
    return HttpResponseRedirect(reverse('register:results', args=(entry.id,)))

class ListView(generic.ListView):
    model = Entry

class DetailView(generic.DetailView):
    model = Entry

class ResultView(generic.DetailView):
    model = Entry
    template_name = 'register/results.html'
