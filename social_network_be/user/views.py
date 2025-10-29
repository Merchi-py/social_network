from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView

from .models import User
from .forms import UserSignUpForm, UserSignInForm

class UserSignUp(CreateView):
    template_name = "user/sign-up.html"
    form_class = UserSignUpForm
    model = User
    success_url = '/'

class UserSignIn(LoginView):
    template_name = 'user/sign-in.html'
    form_class = UserSignInForm
    redirect_authenticated_user = True

class UserSignOut(LogoutView):
    pass

