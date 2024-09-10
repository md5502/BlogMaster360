from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('/accounts/login/')  # Redirect to the login page after successful registration
        else:
            messages.error(request, 'Please correct the errors below.', )
    else:
        form = RegisterForm()
    
    return render(request, 'users/register.html', {'form': form})
