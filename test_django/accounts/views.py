from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(
                request,
                username=username,
                password=password,
            )
            login(request, user)

            return redirect(reverse('app_one:home'))
    else:
        form = RegistrationForm()

    args = {'form':form}
    return render(request, 'accounts/reg_form.html', args)


def view_profile(request, pk=None):
    storage = messages.get_messages(request)
    if pk:
        user = User.objects.get(pk=pk)
    # args = {'user':request.user}
    else:
        user = request.user
    args = {'user':user,'message':storage}
    return render(request, 'accounts/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        form=EditProfileForm(instance=request.user)
        args = {'form':form}
        return render(request, 'accounts/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your New Password has been saved.')
            update_session_auth_hash(request, user=form.user)
            return redirect(reverse('account:view_profile'))
    else:
        form=PasswordChangeForm(user=request.user)

    args = {'form':form}
    return render(request, 'accounts/change_password.html', args)
