from django.db import models
from django.contrib.auth.models import User  # to import the user model from the db

PRIORITIES = (("L", "Low"), ("M", "Medium"), ("H", "High"))


# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # cascade means once the user is deleted delete this particular ToDo
    created_at = models.DateTimeField(
        auto_now=True
    )  # when a model is created it is automatically given this
    priority = models.CharField(choices=PRIORITIES, max_length=20, null=True)
    #
    date = models.DateField(null=True)
    time = models.TimeField(null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
