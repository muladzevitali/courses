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

from apps.cart.models import (CartItem, get_cart_id)
from . import forms
from .models import (User, UserProfile)
from apps.order.models import Order


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

            UserProfile(user=user, profile_picture='users/default-user.png').save()

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
            current_cart_items = CartItem.objects.filter(cart__cart_id=get_cart_id(request)).all()[::1]

            current_variations = [list(item.variations.all()) for item in current_cart_items]

            user_cart_items = CartItem.objects.filter(user=user).all()
            for cart_item in user_cart_items:
                item_variations = list(cart_item.variations.all())
                if item_variations in current_variations:
                    current_cart_item = current_cart_items.pop(current_variations.index(item_variations))

                    cart_item.quantity += current_cart_item.quantity
                    cart_item.save()

            for cart_item in current_cart_items:
                cart_item.user = user
                cart_item.save()

            auth.login(request, user)
            return redirect(request.POST.get('next') or 'dashboard')

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
    orders = Order.objects.filter(user=request.user, is_ordered=True)
    user_profile = UserProfile.objects.get(user=request.user)

    context = dict(orders_count=orders.count(), user_profile=user_profile)
    return render(request, 'user/dashboard.html', context=context)


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


@login_required()
def my_orders(request):
    orders = Order.objects.filter(user=request.user, is_ordered=True).order_by('-created_at')
    context = dict(orders=orders)
    return render(request, 'user/my-orders.html', context=context)


@login_required()
def edit_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    user_form = forms.UserForm(instance=request.user)
    profile_form = forms.UserProfileForm(instance=user_profile)
    if request.method == 'POST':
        user_form = forms.UserForm(request.POST, instance=request.user)
        profile_form = forms.UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, 'Your profile has been updated.')
            return redirect('edit_profile')
        messages.error(request, 'Invalid input.')

    context = dict(user_form=user_form, profile_form=profile_form, user_profile=user_profile)
    return render(request, 'user/edit-profile.html', context=context)


@login_required()
def change_password(request):
    change_password_form = forms.ChangePasswordForm()
    if request.method == 'POST':
        change_password_form = forms.ChangePasswordForm(request.POST)
        if not change_password_form.is_valid():
            messages.error(request, 'Invalid input.')

            return redirect('change_password')

        current_password = change_password_form.cleaned_data['current_password']
        new_password = change_password_form.cleaned_data['new_password']
        user = request.user
        if not user.check_password(current_password):
            messages.error(request, 'Invalid password')

            return redirect('change_password')

        user.set_password(new_password)
        user.save()

        auth.login(request, user)
        messages.success(request, 'Password has been changed successfully')

        return redirect('change_password')

    context = dict(change_password_form=change_password_form)
    return render(request, 'user/change-password.html', context=context)
