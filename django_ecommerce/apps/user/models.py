from secrets import token_hex

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError('Email is required')

        user = self.model(first_name=first_name, last_name=last_name,
                          email=self.normalize_email(email))
        user.generate_username()
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, first_name, last_name, email, password=None):
        user = self.create_user(first_name, last_name, email, password)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.is_active = True

        user.save(using=self.db)


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=30)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    objects = UserManager()

    def __str__(self):
        return f'{self.email} - {self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def generate_username(self):
        self.username = token_hex(6)
        self.save()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def has_module_perms(self, add_label):
        return True


class UserProfile(models.Model):
    user = models.OneToOneField('user.User', on_delete=models.CASCADE)
    address_line_1 = models.CharField(blank=True, max_length=100)
    address_line_2 = models.CharField(blank=True, max_length=100)
    city = models.CharField(blank=True, max_length=20)
    state = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    profile_picture = models.ImageField(blank=True, upload_to='users')

    @property
    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'
