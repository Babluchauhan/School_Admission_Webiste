from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Admission
from .forms import RegisterForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

def login(request):
    # if request.method == 'POST':
    #     # Get email/username and password from form
    #     username = request.POST.get('email')  # or you can name it 'username'
    #     password = request.POST.get('password')
        
    #     # Authenticate the user
    #     user = authenticate(request, username=username, password=password)
        
    #     if user is not None:
    #         # If user exists and password is correct, log them in
    #         auth_login(request, user)
    #         messages.success(request, f'Welcome {user.first_name}!')
    #         return redirect('home')  # redirect to home page
    #     else:
    #         # If authentication fails, show error
    #         messages.error(request, 'Invalid email or password')
    #         return render(request, 'login.html')
    
    # # If GET request, just show the login form
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST': # when user submits the form
        form = RegisterForm(request.POST)

        if form.is_valid(): # if form is valid then save the user
            user = form.save()     # save user in DB
            # login(request, user)   # log user in
            return redirect('login') # redirect to login page after successful registration

    else:
        form = RegisterForm()

    return render(request, 'signup.html', {'form': form})

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