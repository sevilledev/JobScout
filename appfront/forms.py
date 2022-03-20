from email import message
from django import forms
from django.forms.widgets import Textarea
from appfront.models import *

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name', 'type':'text', 'name':'name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email', 'type':'email', 'name':'email'}))    
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Subject', 'type':'text', 'name':'subject'}))
    number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Number', 'type':'text', 'name':'Phone'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write message', 'name':'message'}))
    file = forms.FileField()

    def save_msg(self):
        msg = Contact(
            name=self.cleaned_data['name'],
            subject=self.cleaned_data['subject'],
            email=self.cleaned_data['email'],
            number=self.cleaned_data['number'],
            message=self.cleaned_data['message'],
            file=self.cleaned_data['file'])
        msg.save()