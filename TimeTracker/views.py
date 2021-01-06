from django.shortcuts import render, redirect
from .forms import MyCustomSignupForm
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, "layout/home.html", {})


def signup(request):
    if request.methods == 'POST':
        form = MyCustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/accounts/profile')
    else:
        form = MyCustomSignupForm()

    return render(request, 'account/signup.html', {'form': form})
