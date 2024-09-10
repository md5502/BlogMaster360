from django.urls import include, path

from . import views

app_name = "users"

urlpatterns = [
    path("signup", views.register, name="signup"),
    path("", include("django.contrib.auth.urls")),

]
