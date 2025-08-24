from django.contrib import admin

from .models import User
from .forms import RegistrationForm

admin.register(User)
admin.register(RegistrationForm)
