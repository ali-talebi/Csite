from django.shortcuts import render , redirect
from .forms import LoginForm , SignupForm
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import AccountInformation
# Create your views here.

class SignUpView(View):


    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated :
            return redirect("/")
        return super().dispatch(request, *args, **kwargs)

    form = SignupForm
    template_name = 'Profile/Signup.html'
    def get(self, request):
        return render(request , self.template_name , {'form' : self.form()})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            new_username = form.cleaned_data['username']
            new_email = form.cleaned_data['email']
            new_password = form.cleaned_data['password1']

            user = User.objects.create_user(username = new_username , email = new_email , password = new_password )
            new_profile = AccountInformation(person = user )
            new_profile.save()
            messages.success(request, 'با موفقیت حساب کاربری ساخته شد' , 'success' )
            return redirect('home:home')

        else :
            messages.error(request, 'مشکلی در ساخت حساب کاربری وجود دارد' , 'error' )
            return render(request , self.template_name , {'form' :self.form()})


        return render(request , self.template_name , {'form' : self})

class LoginView(View) :

    template_name = 'Profile/login_page.html'
    form = LoginForm


    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated :
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def setup(self, request, *args, **kwargs):
        self.next = request.GET.get('next' , None )
        return super().setup(request, *args, **kwargs)



    def get(self , request ) :
        return render(request, self.template_name , {'form': self.form()})


    def post(self , request ) :
        new_form = self.form(request.POST)
        if new_form.is_valid() :
            new_username = new_form.cleaned_data['username']
            new_password = new_form.cleaned_data['password']

            user = authenticate(username=new_username, password=new_password)
            if user :
                login(request, user)
                messages.success(request, 'با موفقیت وارد شدید' , 'success')
                if self.next :
                    return redirect(self.next)
                return redirect('home:home')

            else :
                messages.error(request , 'مشکلی در وارد شدن دارید' , 'error')


        return render(request, self.template_name , {'form': self.form()})

class LogOutView(LoginRequiredMixin , View) :
    login_url = '/login/'
    def get(self, request ) :
        logout(request)
        messages.success(request, 'با موفقیت خارج شدید' , 'success')
        return redirect('home:home')




