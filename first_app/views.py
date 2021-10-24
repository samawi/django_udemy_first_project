from django.shortcuts import render
from django.http import HttpResponse

from .models import Topic, WebPage, AccessRecord
from . import forms

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date_accessed')
    date_dict = {'access_records': webpages_list}
    return render(request, 'first_app/index.html', context=date_dict)

def first_form(request):
    form = forms.FirstForm()

    if (request.method == 'POST'):
        form = forms.FirstForm(request.POST)
        if form.is_valid():
            print('Form is valid')
            print('Name: %s' % form.cleaned_data['name'])
            print('Email: %s' % form.cleaned_data['email'])
            print('Text: %s' % form.cleaned_data['text'])

    return render(request, 'first_app/form.html', {'form': form})
