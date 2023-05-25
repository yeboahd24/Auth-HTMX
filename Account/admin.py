from django.contrib import admin
from django import forms

from . import models


class CustomUserAdminForm(forms.ModelForm):

    class Meta:
        model = models.CustomUser
        fields = "__all__"


class CustomUserAdmin(admin.ModelAdmin):
    form = CustomUserAdminForm
    list_display = [
        "last_updated",
        "created",
        "email",
    ]
    readonly_fields = [
        "last_updated",
        "created",
        "email",
    ]


admin.site.register(models.CustomUser, CustomUserAdmin)
