from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('registration/login.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def email_check(user):
    return user.email.endswith('@example.com')

@login_required(login_url='/user')
def updateinfo(request):
    return HttpResponse("Hello world")

def logout_action(request):
    logout(request)
    return redirect(index)

@login_required(login_url='/user')
def home(request) :
    return HttpResponse(loader.get_template('user/home.html').render({}, request))

@login_required(login_url='/user')
def update_view(request):
    current_user = request.user
    email = current_user.email
    first_name = current_user.first_name
    last_name = current_user.last_name
    context  = {
    'email' : email,
    'first_name' : first_name,
    'last_name' : last_name,
    }
    return HttpResponse(loader.get_template('user/update.html').render(context, request))

@login_required(login_url='/user')
def update_action(request):
    if('email' not in request.POST) :
        return redirect(update_view)


    email = request.POST['email']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']

    print(email + ' ' + first_name + ' ' + last_name)
    current_user = request.user
    current_user.email = email
    current_user.first_name = first_name
    current_user.last_name = last_name
    current_user.save()

    context  = {
    'email' : email,
    'first_name' : first_name,
    'last_name' : last_name,
    }

    return HttpResponse("Success")

def login_action(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect(home)
    else:
        # Return an 'invalid login' error message.
        errors = "invalid login"
        template = loader.get_template('registration/login.html')
        context = {
            'errors' : errors,
        }

        return HttpResponse(template.render(context, request))

def register_action(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']

    # TODO catch unique constraint exception 
    user = User.objects.create_user(username=username,email=email,
                                    password=password, first_name=first_name, last_name=last_name)
    user.save()

    print(user.id)

    return redirect(index)

def register_view(request):
    return HttpResponse(loader.get_template('registration/register.html').render({}, request))
