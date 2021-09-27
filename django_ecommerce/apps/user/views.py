from django.contrib import (auth, messages)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import (urlsafe_base64_encode, urlsafe_base64_decode)

from . import forms
from .models import User


def register(request):
    form = forms.UserRegisterForm()

    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(first_name, last_name, email, password)
            user.phone_number = phone_number
            user.save()

            subject = 'Please activate you account'
            message = render_to_string('auth/account_verification_email.html', {
                'user': user,
                'domain': get_current_site(request),
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            email = EmailMessage(subject, message, to=[user.email])
            email.send()

            return redirect(reverse('login') + f'?command=verification&email={user.email}')

    context = dict(form=form)
    return render(request, 'auth/register.html', context=context)


# Create your views here.
def login(request):
    form = forms.UserLoginForm()
    if request.method == 'POST':
        form = forms.UserLoginForm(request.POST)
        if not form.is_valid():
            messages.error(request, 'Invalid login credentials')
            return redirect('login')

        user = auth.authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])

        if user:
            auth.login(request, user)
            return redirect('dashboard')

        messages.error(request, 'Invalid login credentials')
        return redirect('login')

    context = dict(form=form)
    return render(request, 'auth/login.html', context=context)


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect('login')


def user_activation(request, uid, token):
    try:
        pk = urlsafe_base64_decode(uid).decode()
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        pk = -1
    user = get_object_or_404(User, pk=pk)

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Congrats, Your account is active")
        return redirect('login')

    messages.error(request, 'Invalid Activation')
    return redirect('register')


@login_required()
def dashboard(request):
    return render(request, 'auth/dashboard.html')


def forgot_password(request):
    form = forms.ForgotPasswordForm()
    if request.method == 'POST':
        form = forms.ForgotPasswordForm(request.POST)
        if not form.is_valid():
            messages.error(request, "Invalid email")
            return redirect('forgot_password')

        user = User.objects.filter(email__exact=form.cleaned_data['email']).first()
        if user:
            subject = 'Please reset your password'
            message = render_to_string('auth/reset_password_email.html', {
                'user': user,
                'domain': get_current_site(request),
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            email = EmailMessage(subject, message, to=[user.email])
            email.send()

        messages.success(request, "Password reset email has been sent to your email address.")
        return redirect('forgot_password')

    context = dict(form=form)
    return render(request, 'auth/forgot_password.html', context=context)


def reset_password_validate(request, uid, token):
    try:
        pk = urlsafe_base64_decode(uid).decode()
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        pk = -1
    user = get_object_or_404(User, pk=pk)

    if default_token_generator.check_token(user, token):
        request.session['uid'] = uid

        messages.success(request, "Please reset your password")
        return redirect('reset_password')

    messages.error(request, 'Link expired')
    return redirect('login')


def reset_password(request):
    form = forms.ResetPasswordForm()
    if request.method == 'POST':
        form = forms.ResetPasswordForm(request.POST)
        if form.is_valid():
            try:
                pk = urlsafe_base64_decode(request.session['uid']).decode()
            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                pk = -1
            user = get_object_or_404(User, pk=pk)
            user.set_password(form.cleaned_data['password'])

            user.save()
            request.session.delete('uid')

            messages.success(request, 'Password has been reset successfully')
            return redirect('login')

        request.session.delete('uid')

    context = dict(form=form)
    return render(request, 'auth/reset_password.html', context=context)
