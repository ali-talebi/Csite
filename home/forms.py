from django import forms


class DomainSearchForm(forms.Form):

    domain_name  = forms.CharField( help_text="جهت جستجو دامنه مورد نظر را با پیشوند https یا http وارد کنید" , widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'دامنه مورد نظر را وارد کنید'}))
    level_search = forms.IntegerField(help_text="سطح جستجوی خود را با عدد وارد کنید" )

