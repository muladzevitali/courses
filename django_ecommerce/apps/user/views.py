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

from .forms import (UserRegisterForm, UserLoginForm)
from .models import User


def register(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
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
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
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
