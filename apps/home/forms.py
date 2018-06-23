__author__ = 'Merlin'
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    form for contact purpose.
    """
    class Meta:
        model = Contact
        fields = ['name','email','phone','message']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Name [required]'
        self.fields['email'].widget.attrs['placeholder'] = 'Email [required]'
        self.fields['phone'].widget.attrs['placeholder'] = 'Phone'
        self.fields['message'].widget.attrs['placeholder'] = 'Message [required]'
