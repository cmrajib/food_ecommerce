from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
# from django.contrib.auth.views import password_reset
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse

from UserRegistration.forms import SignUpForm
# from UserRegistration.models import Profile
from UserRegistration.models import User


def home(request):
    return HttpResponse('Home')


# def forgot_password(request):
#     if request.method == 'POST':
#         return password_reset(request,
#             from_email=request.POST.get('email'))
#     else:
#         return render(request, 'UserRegistration/forgot_password.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            # messages.success(request, _('Your password was successfully updated!'))
            return redirect('UserRegistration:change_password')
        # else:
        #     messages.error(request, _('Please correct the error below.'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'UserRegistration/change_password.html', {
        'form': form
    })




def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return HttpResponseRedirect(reverse('UserRegistration:login'))

    return render(request,'UserRegistration/signup.html', context={'form': form})


def login_user(request):
    form = AuthenticationForm()

    form.fields['username'].widget.attrs['class'] = "form-control"
    form.fields['password'].widget.attrs['class'] = "form-control"


    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('home:home'))
    return render(request,'UserRegistration/login.html', context={'form':form})

@login_required
def logout_user(request):
    logout(request)
    # messages.warning(request, "You are logged out")
    return HttpResponseRedirect(reverse('home:home'))



# @login_required
# def user_profile(request):
#     profile = Profile.objects.get(user=request.user)
#
#     form = ProfileForm(instance=profile)
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'Profile updated successfully')
#             form = ProfileForm(instance=profile)
#
#     return render( request, 'UserRegistration/change_profile.html', context={'form':form})
