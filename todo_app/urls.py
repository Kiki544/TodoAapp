from django.urls import path
from . import views

urlpatterns = [
    path("logout/", views.logout_user, name="logout"),
    path("", views.home, name="home"),
    # path("goodbye/", views.goodbye, name="bye"),
    path("createtodo/", views.createpost, name="createtodo"),
    path("signup/", views.signUp, name="signup"),
    path("login/", views.loginuser, name="login"),
    path("createtodo", views.createpost, name="createtodo"),
    path(
        "todo/<int:pk>/", views.display_todo, name="displayTodo"
    ),  # passing a FUNCTION,
    path("todo/delete/<int:pk>/", views.delete_todo, name="deletetodo"),
    path("completedtodo/", views.completedtodo, name="completedtodo"),
    path("todo/complete/<int:pk>/", views.complete_todo, name="completetodo"),
    # path("add/", views.add, name="add"),
]
