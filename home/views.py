from django.shortcuts import render, render_to_response
from accounts.forms import RegisterForm, LoginForm
from django.template import RequestContext
from accounts.forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def home(request, template="home/home.html"):
    return render_to_response(template)

def signup(request, template="home/signup.html"):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data['username']
            first_name = cleaned_data['first_name']
            password = cleaned_data['password']
            email = cleaned_data['email']
            user = User(username=username, first_name=first_name, email=email)
            user.set_password(password)
            user.save()
            return HttpResponseRedirect('/login')
    else:
        form = RegisterForm()
    return render_to_response(template, {'form':form}, context_instance=RequestContext(request))

def user_login(request, template='home/login.html'):
    msg = []
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            driver = authenticate(username=username, password=password)
            if driver is not None:
                login(request, driver)
                return HttpResponseRedirect('/dashboard')
            else:
                msg.append("OOPS !! Invalid login details provided")
                return render_to_response(template, {'form': form, 'errors':msg}, context_instance=RequestContext(request))
        
        else:
            return render_to_response(template, {'form': form}, context_instance=RequestContext(request))
    else:
        form = LoginForm()
        context = {'form': form}
        return render_to_response(template, context, context_instance=RequestContext(request))  
