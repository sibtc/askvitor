from django import forms


class ReportForm(forms.Form):
    date = forms.DateField()
