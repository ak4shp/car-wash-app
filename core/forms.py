from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserRegisterationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "email",
            # "first_name",
            # "last_name",
            "password1",
            "password2",
        ]

    def clean(self):
        email = self.cleaned_data.get("email")
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("An Account with that email already exists")
        return self.cleaned_data