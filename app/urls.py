from django.urls import path
from . import views

urlpatterns = [

    path("",views.red),
    path("login",views.login),
    path("random_word", views.random),
    path("form_post",views.contador),
    path("error",views.error),
    path("logout",views.logout),
    path("reset",views.reset)

]