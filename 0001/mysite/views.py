from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.dateformat import format
from django.views import View
from django.views.generic.edit import FormView

from .forms import ReportForm


class Report(FormView):
    template_name = 'report.html'
    form_class = ReportForm

    def form_valid(self, form):
        date = form.cleaned_data.get('date')
        year = date.year
        month = format(date, 'm')
        day = format(date, 'd')
        return redirect('report_details', year, month, day)


class ReportDetails(View):
    def get(self, request, year, month, day):
        users = User.objects.filter(date_joined__year__gte=int(year))
        return render(request, 'report_details.html', {'users': users})
