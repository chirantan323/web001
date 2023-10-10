from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import admin1,vendor,user
from django.contrib import messages
import datetime

def index(request):
    return render(request,'index.html')

def admin_login(request):
    if request.session.has_key('email'):
        del request.session['email']
    if(request.method=="POST"):
        email=request.POST.get('email')
        pw=request.POST.get('password')
        ad=admin1.objects.filter(email=email,password=pw)
        if ad:
            request.session['email']=email
            messages.success(request, 'login sucessfull')
            return redirect('/admin_index')
        else:
            messages.error(request, 'invalid email or password')

    return render(request,'admin_login.html')
#............/!ADMIN LOGIN................

def admin_signup(request):

    d=admin1.objects.all()
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('pass')
        cat=request.POST.get('category')
        at=admin1.objects.filter(email=email)
        if at:
            messages.success(request,'Admin already exist')
        else:
            objatt=admin1.objects.create(name=name,email=email,password=password,category=cat)
            objatt.save()
            messages.success(request,'Admin Added')
    return render(request,'admin_signup.html',{'data':d})

def admin_index(request):
    return render(request,'admin_index.html')

def maintain_user(request):
    d=user.objects.all()
    if request.method=="POST":
        name=request.POST.get('name')
        phno=request.POST.get('phno')
        email=request.POST.get('email')
        password=request.POST.get('pass')
        at=user.objects.filter(userid=email)
        if at:
            messages.success(request,'user already exist')
        else:
            objatt=user.objects.create(name=name,phno=phno,userid=email,password=password)
            objatt.save()
            messages.success(request,'user Added')
    return render(request,'maintain_user.html',{'data':d})

def maintain_vendor(request):
    d=vendor.objects.all()
    if request.method=="POST":
        name=request.POST.get('name')
        phno=request.POST.get('phno')
        email=request.POST.get('email')
        password=request.POST.get('pass')
        cat=request.POST.get('category')
        at=vendor.objects.filter(userid=email)
        if at:
            messages.success(request,'vendor already exist')
        else:
            objatt=vendor.objects.create(name=name,phno=phno,userid=email,category=cat,password=password)
            objatt.save()
            messages.success(request,'vendor Added')
    return render(request,'maintain_vendor.html',{'data':d})

def edit_user(request,id):
    d=user.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get('name')
        phno=request.POST.get('phno')
        email=request.POST.get('email')
        userexist=user.objects.filter(name=name,userid=email,phno=phno)
        if userexist:
            messages.error(request,"Already Exists")
        else:
            d.name=name
            d.userid=email
            d.phno=phno
            #an.anotherfield=value
            d.save()
            messages.success(request,"user edited")
            return redirect('/maintain_user')
    return render(request,'edit_user.html',{'d':d,'id':id})

def edit_vendor(request,id):
    d=vendor.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phno=request.POST.get('phno')
        userexist=user.objects.filter(name=name,userid=email,phno=phno)
        if userexist:
            messages.error(request,"Already Exists")
        else:
            d.name=name
            d.userid=email
            d.phno=phno
            #an.anotherfield=value
            d.save()
            messages.success(request,"vendor edited")
            return redirect('/maintain_vendor')
    return render(request,'edit_vendor.html',{'d':d,'id':id})

def del_user(request,id):
    d=user.objects.get(id=id)
    d.delete()
    return redirect('/maintain_user')

def del_vendor(request,id):
    d=vendor.objects.get(id=id)
    d.delete()
    return redirect('/maintain_vendor')

def user_index(request):
    return render(request,'user_index.html')

def vendorpage(request):
    return render(request,'vendorpage.html')

def catering(request):
    d=vendor.objects.filter(category="catering")
    return render(request,'catering.html',{'d':d})
def lighting(request):
    d=vendor.objects.filter(category="lighting")
    return render(request,'lighting.html',{'d':d})
def decoration(request):
    d=vendor.objects.filter(category="decoration")
    return render(request,'decoration.html',{'d':d})
def flourist(request):
    d=vendor.objects.filter(category="flourist")
    return render(request,'flourist.html',{'d':d})

def user_login(request):
    if request.session.has_key('email'):
        del request.session['email']
    if(request.method=="POST"):
        email=request.POST.get('email')
        pw=request.POST.get('password')
        ad=user.objects.filter(userid=email,password=pw)
        if ad:
            request.session['email']=email
            messages.success(request, 'login sucessfull')
            return redirect('/user_index')
        else:
            messages.error(request, 'invalid email or password')

    return render(request,'user_login.html')

def user_signup(request):
    d=user.objects.all()
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('pass')
        phno=request.POST.get('phno')
        at=user.objects.filter(userid=email)
        if at:
            messages.success(request,'user already exist')
        else:
            objatt=user.objects.create(name=name,phno=phno,userid=email,password=password)
            objatt.save()
            messages.success(request,'Admin Added')
    return render(request,'user_signup.html',{'data':d})





# Create your views here.
