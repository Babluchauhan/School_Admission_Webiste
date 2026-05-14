from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Admission

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def admission_form(request):
    #Fix this form make it short and simple
    if request.method == 'POST':
        # Get form data from POST request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('dob')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        # Create new Admission object and save to database
        admission = Admission(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=gender,
            email=email,
            phone=phone
        )
        admission.save()
        
        # Show success message
        #you need to add messages in settings.py and base.html to show this message
        messages.success(request, 'Application submitted successfully!')
        
        # Redirect to home page
        return redirect('home')
    else:
        # Just show the form
        return render(request, 'admission_form.html')