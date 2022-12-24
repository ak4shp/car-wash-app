from django.contrib.auth import (
    views as auth_views,
    get_user_model
)
from django.contrib import messages
from django.shortcuts import redirect, render

from core.forms import UserRegisterationForm


class MyLogoutView(auth_views.LogoutView):
    template_name = 'registration/logout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def register(request):
    User = get_user_model()

    if request.method == "POST":
        form = UserRegisterationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            if User.objects.filter(username=username).first():
                messages.warning(request, f"Username '{username}' already used.")
                return redirect("register")
            if User.objects.filter(username=username).first():
                messages.warning(request, f"Email '{email}' already used.")
                return redirect("register")
            user = form.save()
            user.save()
            messages.success(
                request,
                f"Account has been created for {user.username}",
            )
            return redirect("login")
    else:
        form = UserRegisterationForm()

    context = {"form": form, "page": "Register"}
    return render(request, "registration/register.html", context=context)


