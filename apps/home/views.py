from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.views import generic
from django.contrib.sites.shortcuts import get_current_site

from .forms import ContactForm
from .models import Contact


class HomeView(generic.CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'home.html'

    def form_valid(self, form):
        form = form.save(commit=False)
        mail_subject = 'J-Guard : Contact Form Submission Succesful!'
        message = render_to_string('contact_response.html', {
            'user': form.name,
        })
        to_email = form.email
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
        )
        email.send()

        mail_subject2 = 'J-Guard : Enquiry Received!'
        message2 = render_to_string('contact.html', {
            'user': form.name,
            'message': form.message,
            'phone': form.phone,
            'email': form.email,
        })
        email2 = EmailMessage(
                    mail_subject2, message2, to=['jguard.services@gmail.com', 'mermat07@gmail.com']
        )
        email2.send()

        form.save()
        messages.success(self.request, "Oh Great! Your Response Has Been Recorded!")
        return HttpResponseRedirect('#write')

    def form_invalid(self, form):
        return HttpResponseRedirect('#write')



