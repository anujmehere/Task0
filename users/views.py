from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate,login,logout
from .forms import PostForm

def Login(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            if not username or not password:
                messages.success(request, 'Both Username and Password are required.')
                return redirect('/login/')
            user_obj = User.objects.filter(username = username).first()
            if user_obj is None:
                messages.success(request, 'User not found.')
                return redirect('/login/')
        
        
            user = authenticate(username = username , password = password)
            
            if user is None:
                messages.success(request, 'Wrong password.')
                return redirect('/login/')
        
            login(request , user)
            return redirect('/')

                
            
            
    except Exception as e:
        print(e)
    return render(request , 'login.html')



def Register(request):
    try:
        if request.method == 'POST':
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken.')
                return redirect('/register/')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/register/')
            
            user_obj = User(username = username , email = email)
            user_obj.set_password(password)
            user_obj.save()
    
            profile_obj = Profile.objects.create(firstname=firstname,lastname=lastname,password=password ,email=email,username=username)
            profile_obj.save()
            return redirect('/login/')

        except Exception as e:
            print(e)

    except Exception as e:
            print(e)

    return render(request , 'register.html')


def Logout(request):
    logout(request)
    return redirect('/')


def Home(request):
    return render(request , 'home.html')


def addpost(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Submitted.')
            return redirect('addpost')
    context = {
        'form': form
    }
    return render(request, 'addpost.html', context)

from .models import Post

def posts(request):
    posts = Post.objects.all()
    param = {'posts': posts}
    return render(request, 'blogs.html',param )