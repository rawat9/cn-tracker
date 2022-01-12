from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import Group, User
from django.contrib import messages, auth
from .decorators import unauthenticated_user

# Create your views here.

def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('users')
        else:
            messages.warning(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'authentication/login.html')


@unauthenticated_user
def register(request):

    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username exists')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                user.save()

                group = Group.objects.get(name='ninja')
                user.groups.add(group)

                messages.success(request, 'Account created successfully')
                return redirect('login')        
        
        else: 
            messages.error(request, 'Password do not match')
            return redirect('register')

    return render(request, 'authentication/register.html')

def logout_user(request):
    logout(request)
    return redirect('login')