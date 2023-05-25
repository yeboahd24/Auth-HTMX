from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager



class AccountManager(BaseUserManager):
    def create_user(self, email,password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    email = models.EmailField(unique=True)


    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Account_CustomUser_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Account_CustomUser_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("Account_CustomUser_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("Account_CustomUser_htmx_delete", args=(self.pk,))
