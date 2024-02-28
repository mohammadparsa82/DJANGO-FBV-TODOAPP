from django.urls import path
from accounts.views import * 

app_name = 'accounts'

urlpatterns = [
    path('login/',LoginView, name='login'),
    path('register/',RegisterView,name='register'),
    path("logout", LogoutView, name="logout"),
]