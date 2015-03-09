from django import forms
from django.contrib import auth
from django.forms import ModelForm
from core.models import Feedback, Reviews, Deliveryaddress

class FeedbackForm(forms.ModelForm):

    class Meta:
        # Set this form to use the model
        model = Feedback

class ReviewForm(forms.ModelForm):
    RATING_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    class Meta:
        # Set this form to use the model
        model = Reviews

        # Exclude the fields of Form.
        exclude = ('item','user')

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'placeholder': field.label,
                    'class': 'form-control'
                    })
        self.fields['rating'].widget = forms.RadioSelect(choices=self.RATING_CHOICES)

class DeliveryAddressForm(forms.ModelForm):

    class Meta:
        # Set this form to use the model
        model = Deliveryaddress

        # Exclude the fields of Form
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(DeliveryAddressForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget.attrs.update({
                    'placeholder': field.label,
                    'class': 'form-control'
                    })
