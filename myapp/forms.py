from django import forms

from .models import Contacts

class ContactForm(forms.Form):
    class Meta:
        model = Contacts()
        fields = ['name', 'email','subject', 'message']