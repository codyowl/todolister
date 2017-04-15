from django.shortcuts import render, render_to_response

# Create your views here.
def home(request, template="home/home.html"):
    return render_to_response(template)

def signup(request, template="home/signup.html"):
	return render_to_response(template)

def login(request, template="home/login.html"):
	return render_to_response(template)	    
