from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

from .forms import ContactForm

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def about_us(request):
    return render(request, 'core/about_us.html')

def services(request):
    return render(request, 'core/services.html')

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            message = name+": "+message
            try:
                send_mail(subject, message, email, ['contactsactive@gmail.com', 'aimerashu@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Thanks for contacting us!')
            return render(request, 'core/index.html')
    else:
        form = ContactForm()

    return render(request, 'core/email.html', {'form': form})
