from django.http import HttpResponse
from django.shortcuts import render
from.forms import *
from django.contrib.auth.forms import UserCreationForm
from core.forms import ContactForm
from core.models import Contact
from django.contrib import messages

def home(request):
    return render(request, 'core/home.html')


def contact(request):
    form = ContactForm()
    # Ensures that submit button has been clicked!
    if request.method == 'POST':
        # form with data
        form = ContactForm(request.POST)
        # checking if form validation is correct
        if form.is_valid():
            # getting input data
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            # storing the data in Contact Model
            Contact.objects.create(name=name, email=email, message=message)
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})
def register_user(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
     messages.error(request,'correct the errors')
     form=UserCreationForm()
     return render(request, 'registration/register.html',{'form':form})
