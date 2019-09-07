from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import DashReg, UpdateForm, ProfileUpdateForm
from django.contrib import messages
# Create your views here.

def register(request):

    if request.method == 'POST':
        form = DashReg(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            messages.success(request, f'Registration successful for {first_name} {last_name} as {username}')
            return redirect('login')
    else:
        form = DashReg()
    return render(request, 'users/register.html', {'form': form})

@login_required()
def profile(request):
    if request.method == 'POST':
        uForm = UpdateForm(request.POST, instance=request.user)
        pForm = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if uForm.is_valid() and pForm.is_valid():
            uForm.save()
            pForm.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')

    else:
        uForm = UpdateForm(instance=request.user)
        pForm = ProfileUpdateForm(instance=request.user.profile)


    context = {'uForm':uForm,
               'pForm':pForm}

    return render(request, 'users/profile.html', context)



