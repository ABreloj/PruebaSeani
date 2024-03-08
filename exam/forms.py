from django import forms

from career.models import Career
from .models import Stage

class CandidateForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)
    stage = forms.ModelChoiceField(queryset=Stage.objects.all())
    career = forms.ModelChoiceField(queryset=Career.objects.all())