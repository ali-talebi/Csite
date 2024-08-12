from django  import forms
from .models import Register_Time_Enter

class RecordTime(forms.ModelForm):
    class Meta:
        model = Register_Time_Enter
        fields = ['date'  , 'status' , 'description' ]