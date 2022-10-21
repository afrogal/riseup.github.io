from django.urls import path
from . import views

appName = 'budgetproApp'

urlpatterns = [
    path('',views.registerUser, name='registerUser'),
    #path('handleSignup/',views.handleSignup,name='handleSignup')
]
