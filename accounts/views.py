from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout
from .forms import CustomUserForm

def signup_view(request):
    username_errors = None  # Inicializa la variable para almacenar los errores del campo "username"

    if request.method == "POST":
        form = CustomUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
        else:
            # Verifica si el error "username ya en uso" está presente en el formulario
            if 'username' in form.errors:
                username_errors = form.errors['username']
    else:
        form = CustomUserForm()

    return render(request, "accounts/signup.html", {"form": form, "username_errors": username_errors})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")

    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("index")
    
