from django.shortcuts import render,redirect

from .forms import CustomUserCreationForm , EditPasswordForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login ,authenticate ,logout
from .models import Profile , Exercise
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from passlib.handlers.django import django_pbkdf2_sha256
# Create your views here.
from django.contrib import messages

def registerUser(request,):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            profile = Profile.objects.get(user=user)
            return redirect('login')
    return render(request,"register.html",{"form":form})

def loginUser(request):


    if request.user.is_authenticated:
        return redirect('register')


    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request,'Username does not exist')
        user = authenticate(request,username=username,password=password,email=email)
        if user is not None:
            login(request,user)
            profile = Profile.objects.get(user=user)
            return redirect("register")
        else:
            messages.error(request,'Username or password is incorrect')
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect ("login")

def account(request,pk):
    user = User.objects.get(id=pk)
    profile = Profile.objects.get(user=user)
    form = EditPasswordForm()
    formprofile = ProfileForm(instance=profile)

    context = {"profile" : profile,"form":form,"formprofile":formprofile}
    return render(request,"account.html",context)


def update_profile(request,pk):
    user = User.objects.get(id=pk)
    profile = Profile.objects.get(user=user)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            user.first_name=request.POST['name']
            user.last_name=request.POST['last_name']
            user.email=request.POST['email']
            user.username=request.POST['username']
            user.save()
            form.save()
            messages.success(request,"ACCOUNT UPDATED")
            return redirect("login")
        
    context ={'form':form}
    return render(request,"edit_profile.html",context)


def delete_account(request,pk):
    profile = Profile.objects.get(id=pk)

    if request.method=='POST':
        profile.delete()
        messages.success(request, "Account deleted!" )     
        return redirect("register")

    return render(request,"delete_user.html")
    

def change_password(request,pk):
    form = EditPasswordForm()
    
    if request.method=='POST':
        form = EditPasswordForm(request.POST)
        if form.is_valid():
            password1 = request.POST['password1']  
            old_password=request.POST['oldpassword'] 
            user = User.objects.get(id=pk)
            current_password=user.password    
            equality=check_password(old_password,current_password)
            if equality  :    
                    user.set_password(password1)
                    user.save()
                    logout(request)
                    return redirect('login')
            messages.success(request, "Old password must match with the current one!" )  
        else:
            messages.success(request,"Passwords must match")
    return render(request,'change_password.html',{"form":form})
    



def exercise(request,pk):
    ex=Exercise.objects.get(id=pk)

    return render(request,"exercise_id.html",{"ex":ex})
def solve(request,pk,pk2):
    if request.method=='POST':
        ex1 = request.POST['ex1']
        ex2 = request.POST['ex2']
        Owner = Exercise.objects.get(id=pk)
        user = User.objects.get(id=pk2)
        profile=Profile.objects.get(user=user)
        answer1 = Owner.Answer1default
        answer2 = Owner.Answer2default

        if answer1==ex1  and answer2==ex2:
            profile.exercises.add(Owner)
            Owner.owner.add(profile)
            return render(request,"congrats.html")
        else:
                return render(request,"fail.html")
        

def exercises_solved(request,pk):
    user = User.objects.get(id=pk)
    profile=Profile.objects.get(user=user)

    all_exercises=[]
    all_exercises=Exercise.objects.filter(owner=profile)
  
    return render(request,"exercises_solved.html",{"all_exercises":all_exercises})


def list_of_exercises(request,pk):
    if request.method=='POST':
        user=User.objects.get(id=pk)
        profile=Profile.objects.get(user=user)
        rez = request.POST['dificulty']
        list = Exercise.objects.filter(dificulty=rez)
        list = list.exclude(owner=profile)

        return render(request,"list_type.html",{'rez':rez,'list':list})
