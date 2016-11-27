from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy

from . import models


def index(request):
    return render(request, 'cash/index.html')


class NewActivity(CreateView):
    model = models.Activity
    fields = ['description', 'time', 'activity_type', 'value']
    template_name = 'cash/new_cash_activity.html'
    success_url = reverse_lazy('cash:activity_list')


class ActivityList(ListView):
    model = models.Activity
