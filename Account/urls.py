from django.urls import path, include
from rest_framework import routers

from . import api
from . import views
from . import htmx


router = routers.DefaultRouter()
router.register("CustomUser", api.CustomUserViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("Account/CustomUser/", views.CustomUserListView.as_view(), name="Account_CustomUser_list"),
    path("Account/CustomUser/create/", views.CustomUserCreateView.as_view(), name="Account_CustomUser_create"),
    path("Account/CustomUser/detail/<int:pk>/", views.CustomUserDetailView.as_view(), name="Account_CustomUser_detail"),
    path("Account/CustomUser/update/<int:pk>/", views.CustomUserUpdateView.as_view(), name="Account_CustomUser_update"),
    path("Account/CustomUser/delete/<int:pk>/", views.CustomUserDeleteView.as_view(), name="Account_CustomUser_delete"),

    path("Account/htmx/CustomUser/", htmx.HTMXCustomUserListView.as_view(), name="Account_CustomUser_htmx_list"),
    path("Account/htmx/CustomUser/create/", htmx.HTMXCustomUserCreateView.as_view(), name="Account_CustomUser_htmx_create"),
    path("Account/htmx/CustomUser/delete/<int:pk>/", htmx.HTMXCustomUserDeleteView.as_view(), name="Account_CustomUser_htmx_delete"),
)
