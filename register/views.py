from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse

from datetime import date

from .models import Entry

# Create your views here.
def index(request):
    admission_years = list(range(2021, 1975, -1))
    entry_dates = [date(2021, 9, day) for day in [10, 11, 12, 13]]
    context = {
        'title': '参加登録',
        'admission_years': admission_years,
        'entry_dates': entry_dates,
    }
    return render(request, 'register/index.html', context)

def submit(request):
    fields = ['screen_name', 'admission_year', 'start_date', 'end_date']
    entry = Entry.objects.create(**{k: request.POST[k] for k in fields})
    return HttpResponseRedirect(reverse('register:results', args=(entry.id,)))

class ListView(generic.ListView):
    model = Entry

    def get_ordering(self, **kwargs):
        return '-admission_year'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = '登録一覧'
        return context

class DetailView(generic.DetailView):
    model = Entry

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = '登録内容'
        context['message'] ='以下の内容で登録されています'
        return context

class ResultView(generic.DetailView):
    model = Entry

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = '登録結果'
        context['message'] ='以下の内容で登録されました'
        return context
