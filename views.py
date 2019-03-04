from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, ListView, DeleteView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Sitreps
from django.utils import timezone
from django.urls import reverse

# Create your views here.
def index2(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    # View code here...
    return render(request, 'sitreps/index.html', {})

class SitrepsListView(ListView):

    template_name = 'sitreps/list.html'
    model = Sitreps
    queryset= Sitreps.objects.all()
    context_object_name = 'sitreps'
    paginate_by=10


class SitrepsDetailView(DetailView):

    model = Sitreps
    template_name = 'sitreps/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class SitrepsCreateView(CreateView):
    model = Sitreps
    fields = ['title','text']
    template_name = 'sitreps/create.html'
    success_url="/sitreps"
    initial={'text':'Initial text'}

class SitrepsUpdateView(UpdateView):
    model = Sitreps
    fields = ['title','text']
    template_name = 'sitreps/create.html'
    success_url="/sitreps"
