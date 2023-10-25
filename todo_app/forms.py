from django import forms
from .models import Todo


# class TodoForm(forms.Form):
#     firstname = forms.CharField(max_length=50)
#     lastname = forms.CharField(max_length=50)
#     email = forms.EmailField()
#     username = forms.CharField(max_length=20)


#     class Meta:
#         fields = ("firstname", "lastname", "email", "username")
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        # fields = "__all__"
        fields = ["title"]  # to make the create show onlu the title


# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=50)
#     password = forms.CharField(max_length=100)
