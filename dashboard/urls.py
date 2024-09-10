from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index' ),
    path("create_post", views.create_post, name='create_post'),
    path("delete_post/<slug:slug>", views.delete_post, name='delete_post'),
    path("update_post/<slug:slug>", views.update_post, name='update_post'),
    path("edit_profile", views.edit_profile, name='edit_profile'),
]