from django.shortcuts import render
from .models import Books


# Create your views here.
def index(req):
    allbooks = Books.objects.all()
    print(allbooks)
    # b=Books.objects.create(bookid=118,title='mongodb',author='mm',category='database',price=3000,qty=3,dop='2000-02-21',photo=None)
    # b.save
    # b=Books.objects.get(bookid=110).first()
    # b.author='aditi'
    # b.author='aditi'
    # b.save() 
    # b=Books.objects.filter(bookid=110).first()
    context={'allbooks':allbooks}
    return render(req, "index.html",context)


def signup(req):
    return render(req, "signup.html")


def signin(req):
    return render(req, "signin.html")


def about(req):
    return render(req, "about.html")


def contact(req):
    return render(req, "contact.html")


from datetime import datetime


def DTLdemo(req):
    # name="vedant"
    # return render(req, "DTLdemo.html",{'name':name})

    name = "vedant"
    curdatetime = datetime.now()
    greeting = "Good evening"
    curhour = datetime.now().hour
    print(curhour)
    password = "admin"
    authors = ["pp", "jj", "cc"]
    students = {
        101: {"name": "pooja", "issuedbook": "python"},
        102: {"name": "raj", "issuedbook": "java"},
    }
    context = {
        "name": name,
        "curdatetime": curdatetime,
        "greeting": greeting,
        "password": password,
        "curhour": curhour,
        "authors": authors,
        "students": students,
    }

    return render(req, "DTLdemo.html", context)
