import shutil

from django.shortcuts import render, redirect

from socialmediaapp.settings import LOGIN_REDIRECT_URL
from .management.commands.dataload import Command
from .models import Item, MyPosts, MyInformation, MyLikes
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect as httpRequest
from django.core.files.storage import FileSystemStorage
import requests
# Create your views here.

def home(request):
    command = Command()
    item = Item.objects.all()
    userName = str(request.user)
    print(userName)
    #print(requests.get(LOGIN_REDIRECT_URL))
    try:
        if "sumit" in userName:
            return redirect('main_view')
        return render(request, "socialapps/home.html", {'item':item})
    except:
        return redirect('login')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup')
    else:
        form = UserCreationForm()
    return render(request, "socialapps/signup.html", {'form':form})

def login(request):
    print(request.GET)
    # if request.method == 'POST':
    #     form = AuthenticationForm(data=request.POST)
    #     if form.is_valid():
    #         user = form.get_user()
    #         auth_login(request, user)
    #         return redirect('main_view')
    # else:
    #     form = AuthenticationForm()
    # if request.method=="POST":
    #     logout(request)

    userName = str(request.user)
    if "sumit" in userName:
        return render(request, "socialapps/mainview.html", {'some_flag':True})

    return render(request, 'socialapps/login.html')

@login_required
def main_view(request):
    userName = str(request.user)
    if "sumit" in userName:
        return render(request, 'socialapps/mainview.html', {'some_flag':False})
    else:
        return render(request, 'socialapps/login.html')

@login_required
def fb(request):
    if request.method =='POST':
        try:
            shutil.rmtree('media')
        except:
            print("media is not here")
        upload_image=request.FILES['document']
        fs = FileSystemStorage()
        fs.save(upload_image.name, upload_image)
    item = Item.objects.all()
    command = Command()
    myPosts = MyPosts.objects.all()
    myInformation = MyInformation.objects.all()
    myLikes = MyLikes.objects.all()
    command.handle()
    return render(request, 'socialapps/fb.html', {'item':item, 'myPosts':myPosts, 'myInformation':myInformation, 'myLikes':myLikes})

def logoutuser(request):
    print(User.objects.get(username = str(request.user)))
    u = User.objects.get(username = str(request.user))
    u.delete()
    if request.method=="GET":
        logout(request)
    return render(request, 'socialapps/home.html')
