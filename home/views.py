from django.shortcuts import render , redirect
from django.views import View
from account.models import Profile
from .models import  Register_Time_Enter
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecordTime
from django.contrib import messages
# Create your views here.



class ShowDetailView(LoginRequiredMixin, View):


    template_name = 'detail_record.html'

    def setup(self, request, *args , id , **kwargs):
        self.data = Register_Time_Enter.objects.get( id = id )
        return super().setup(request, *args , id , **kwargs )


    def get(self ,request , id ) :
        return render(request , self.template_name , {'data' : self.data })


class HomeView(LoginRequiredMixin , View):
    template_name = 'home.html'

    def setup(self, request, *args, **kwargs):
        if request.user.is_authenticated :
            self.find_profile = Profile.objects.get( person__username =request.user.username  )
            self.times = Register_Time_Enter.objects.filter(person_user = self.find_profile )

        return super().setup(request, *args, **kwargs )



    def get(self ,request ) :
        return render(request , self.template_name  , {'client' : self.find_profile , 'times' : self.times} )



class RecordTimeView(LoginRequiredMixin , View):


    record_form = RecordTime
    template_name = 'record_time.html'
    def get(self,request,*args ,**kwargs ) :
        return render(request , self.template_name , {'form':self.record_form})

    def post(self,request) :
        form = self.record_form(request.POST )
        if form.is_valid() :
            model_save = form.save(commit=False)
            model_save.person_user = Profile.objects.get( person__username =request.user.username )
            model_save.save()
            messages.success(request, 'با موفقیت اضافه شد' , 'success')
            return redirect('home:home')

        return render(request , self.template_name , {'form':self.record_form} )