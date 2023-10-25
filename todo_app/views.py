from django.shortcuts import render, HttpResponse, redirect
from .models import Todo, Comment
from .forms import TodoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

# Create your views here.


@login_required(login_url="/login")
def home(request):
    # data = {"message": "this is to inform you", "info": "246"}
    todos = Todo.objects.filter(completed=False)
    data = {"todos": todos}
    return render(request, "home.html", context=data)


def loginuser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("")
        else:
            return render(
                request, "auth/login.html", context={"message": "Account not found"}
            )

    return render(request, "auth/login.html")


def signUp(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("")

    return render(request, "auth/signup.html", context={"form": form})


@login_required(login_url="/login")
def createpost(request):
    form = TodoForm()
    # Username = request.POST
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            result = form.save(
                commit=False
            )  # only works for forms connected to a model
            result.author = request.user
            result.completed = False
            result.save()
            return redirect("")
        print("firstname")

    return render(request, "createtodo.html", {"forms": form})


@login_required(login_url="/login")
def display_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    comments = Comment.objects.filter(todo=todo)
    if request.method == "POST":
        comment = request.POST.get("comment")

        if comment:
            author = request.user
            data = Comment(comment=comment, author=author, todo=todo)
            data.save()
    return render(
        request, "displayTodo.html", context={"todo": todo, "comments": comments}
    )


@login_required(login_url="/login")
def completedtodo(request):
    todos = Todo.objects.filter(completed=True)

    return render(request, "completed_todo.html", context={"todos": todos})


@login_required(login_url="/login")
def logout_user(request):
    logout(request)
    return redirect("/login")


@login_required(login_url="/login")
def delete_todo(request, pk):
    Todo.objects.get(pk=pk).delete()
    return redirect("")


@login_required(login_url="/login")
def complete_todo(request, pk):
    Todo.objects.filter(pk=pk).update(completed=True)
    return redirect("/home")


# def goodbye(request):
