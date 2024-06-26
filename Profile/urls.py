from django.urls import path
from .views import LoginView , LogOutView , SignUpView


app_name = 'Profile'
urlpatterns = [
    path('login/' , LoginView.as_view(), name='login' )  ,
    path('logout/', LogOutView.as_view(), name='logout') ,
    path('signup/', SignUpView.as_view(), name='signup') ,

]