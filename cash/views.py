from django.shortcuts import render
from django.views.generic import CreateView

from . import models


def index(request):
    return render(request, 'cash/index.html')


class NewActivity(CreateView):
    model = models.Activity
    fields = ['description', 'time', 'activity_type', 'value']
    template_name = 'cash/new_cash_activity.html'
