from urllib import request

from django.shortcuts import render ,redirect
from django.views import View
from .forms import LoginForm
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages


# Create your views here.


class LoginView(View):
    template_name = 'login.html'

    login_form = LoginForm

    def get(self, request):
        return render(request , self.template_name , {'form' : self.login_form } )


    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            n_username = form.cleaned_data['username']
            n_password = form.cleaned_data['password']

            user = authenticate(request, username=n_username, password=n_password)
            if user :
                login(request, user)
                messages.success(request, 'با موفقیت وارد شدید' , 'success')
                return redirect('home:home' )

        return render(request , self.template_name , {'form' : self.login_form }  )





class LogoutView(View):

    def get(self , request ):
        logout(request)
        return redirect('account:login')