from django.shortcuts import render, HttpResponse, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def home(request):
    return render(request, "survey/index.html")


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'survey/register.html', context)


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'survey/login.html')
