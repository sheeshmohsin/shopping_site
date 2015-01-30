from django import forms
from django.contrib import auth
from django.forms import ModelForm
from core.models import Feedback

class FeedbackForm(forms.ModelForm):

    class Meta:
        # Set this form to use the model
        model = Feedback