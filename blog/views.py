from django.shortcuts import render
def index(request):
    return render(request,"index.html",context={})
from django.shortcuts import render


def about(request):
    return render(request,"about.html",context={})

def h404(request):
    return render(request,"404.html",context={})

def contact(request):
    return render(request,"contact.html",context={})

def courses(request):
    return render(request,"courses.html",context={})
def team(request):
    return render(request,"team.html",context={})

def testimonial(request):
    return render(request,"testimonial.html",context={})
# Create your views here.
