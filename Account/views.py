from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class CustomUserListView(generic.ListView):
    model = models.CustomUser
    form_class = forms.CustomUserForm


class CustomUserCreateView(generic.CreateView):
    model = models.CustomUser
    form_class = forms.CustomUserForm


class CustomUserDetailView(generic.DetailView):
    model = models.CustomUser
    form_class = forms.CustomUserForm


class CustomUserUpdateView(generic.UpdateView):
    model = models.CustomUser
    form_class = forms.CustomUserForm
    pk_url_kwarg = "pk"


class CustomUserDeleteView(generic.DeleteView):
    model = models.CustomUser
    success_url = reverse_lazy("Account_CustomUser_list")
