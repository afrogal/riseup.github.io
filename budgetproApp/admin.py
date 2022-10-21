from django.contrib import admin
from django.contrib.sessions.models import Session
admin.site.register(Session)
from .models import UserProfile
admin.site.register(UserProfile)

# Register your models here.
