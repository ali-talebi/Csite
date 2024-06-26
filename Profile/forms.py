from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User





class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام کاربری' , 'class': 'form-control'} ))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':  'رمز عبور' , 'class': 'form-control'}))



class SignupForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام کاربری' , 'class': 'form-control' } ))
    email    = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'ایمیل کاربری' , 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور' , 'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'تایید رمز عبور' , 'class': 'form-control'}))

    def clean_email(self ):
        t = self.cleaned_data['email']
        if User.objects.filter(email=t).exists() :
            raise ValidationError('این ایمیل قبلا انتخاب شده است')

        return t


    def clean_username(self):
        t = self.cleaned_data['username']
        if User.objects.filter(username=t).exists() :
            raise ValidationError("نام کاربری تکراری میباشد")
        return t

    def clean(self):
        cleaned_data = super().clean()
        password2    = cleaned_data.get("confirm_password")
        password1 = cleaned_data.get("password")

        if password1 != password2 and password1 and password2 :
            raise ValidationError("رمز های عبور با هم یکسان نیست")

        return password2

    def save(self , commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])

        if commit :
            user.save()

        return user




