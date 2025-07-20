from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def register(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            login(req, form.save())
            return redirect('posts') 
    else:
        form = UserCreationForm()
    return render(req, 'register.html', {'form':form})

def user_login(req):
    if req.method == 'POST':
        form = AuthenticationForm(data=req.POST)
        if form.is_valid():
            login(req, form.get_user())
            if 'next' in req.POST:
                return redirect(req.POST.get('next')) 
            else:
                return redirect('new_post') 
    else:
        form = AuthenticationForm()
    return render(req, 'login.html', {'form':form})

def user_logout(req):
    if req.method == 'POST':
        logout(req)
        return redirect('posts') 