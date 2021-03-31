from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegForm, updateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


def register(request):
    if request.method == "POST":
        form = UserRegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            try:
                validate_password(password, username)
                form.save()
                return redirect('home')
            except ValidationError as e:
                form.add_error('password1', e)
                return render(request, 'user/register.html', {'form': form})
    else:
        form = UserRegForm()

    return render(request,
                  'user/register.html',
                  {
                      'title': 'Регистрация',
                      'form': form,
                  }
                  )

@login_required
def profile(request):
    if request.method == 'POST':
        updateUser = updateUserForm(request.POST, instance=request.user)
        if updateUser.is_valid():
            updateUser.save()
            messages.success(request, f'Ваш профиль был успешно изменен')
            return redirect('profile')
    else:
        updateUser = updateUserForm(instance=request.user)

    data = {
        'updateUserForm': updateUser,
        'title': 'Личный кабинет'
    }

    return render(request, 'user/profile.html', data)

def create(request):
    return render(request, 'user/create.html')