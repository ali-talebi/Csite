from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username' , widget=forms.TextInput )
    password = forms.CharField(label='password' , widget=forms.PasswordInput )


