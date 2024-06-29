from urllib import request

from django.shortcuts import render , redirect
from .models import Search_Domain , Guideline
from django.views import View
from .forms import DomainSearchForm
from .get_data_with_link import GET_DATA_WITH_LINK_FUNC
from django.contrib import messages
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
import time
import requests
from bs4 import BeautifulSoup
# Create your views here.






class HomeView(View):

    form = DomainSearchForm
    template_name = 'index.html'


    def setup(self, request, *args , page=1 , **kwargs):
        try :
            self.total_search = Search_Domain.objects.all()
            self.paginator = Paginator(self.total_search , 3 )
            self.total_data = self.paginator.page(page)

        except EmptyPage:
            self.total_data = self.paginator.page(self.paginator.num_pages)

        except PageNotAnInteger:
            self.total_data = self.paginator.page(1)

        return super().setup(request, *args, **kwargs)

    def get(self, request , page = 1 ):
        return render(request , self.template_name , {'form': self.form , 'data':self.total_data})


    def post(self, request , page = 1  ):
        form = self.form(request.POST)
        if form.is_valid():
            level_search = form.cleaned_data['level_search']
            domain = form.cleaned_data['domain_name']
            try :
                first_status_code , first_a_link , first_s_ , first_server_name = GET_DATA_WITH_LINK_FUNC(domain)

                if level_search == 1 :

                    new_instance = Search_Domain(domain_name=domain , serch_level = 1 ,  status = first_status_code , total_text= first_s_ , total_link=first_a_link , server=first_server_name  , summary="No summer" , classify = "Not Determined"  )
                    new_instance.save()
                    messages.success(request, "با موفقیت جستجو انجام شد" , 'success')


                elif level_search == 2 :
                    try:
                        second_status_code = None
                        second_a_link  = []
                        second_s_ = []
                        second_server_name  = None

                        for link in first_a_link :
                            sub_second_status_code , sub_second_a_link , sub_second_s_ , sub_second_server_name = GET_DATA_WITH_LINK_FUNC(link)
                            for sub_link in sub_second_a_link :
                                second_a_link.append(sub_link)
                            second_s_.append(sub_second_s_)

                        for i in second_a_link :
                            first_a_link.append(i)


                        for i in second_s_ :
                            first_s_ += f"{i} . "
                    except Exception as e:
                        messages.error(request , e , 'error' )
                        return redirect('home:error' )
                    finally:
                        new_instance = Search_Domain(domain_name=domain , serch_level = 2 ,  status = first_status_code , total_text= first_s_ , total_link=first_a_link , server=first_server_name  , summary="No summer" , classify = "Not Determined"  )
                        new_instance.save()
                        messages.success(request, "با موفقیت جستجو انجام شد" , 'success')
                        return redirect('home:home' )

            except Exception as e:
                messages.error(request , e , 'error' )
                return redirect('home:error' )

        else :
            messages.error(request, "خطایی وجود دارد " , 'error')


        return render(request , self.template_name, {'new_instance' : new_instance , 'data':self.total_data})


class DetailView(View) :

    template_name = 'result_answer.html'

    def setup(self, request, *args, id ,  **kwargs):
        self.data = Search_Domain.objects.get(id  = id )
        self.links = []

        link_data = self.data.total_link
        for i in link_data.split(','):
            self.links.append(i)


        return super().setup(request, *args, **kwargs)


    def get(self , request ,id ) :
        return render(request , self.template_name, {'data': self.data , 'links': self.links})


    def post(self , request , id ):
        return render(request , self.template_name, {'data': self.data , 'links': self.links})



class GuideView(View) :

    template_name = 'guide.html'

    def setup(self, request , *args , **kwrags ) :
        self.data = Guideline.objects.all()
        return super().setup(request , *args , **kwrags )

    def get(self , request ) :
        return render(request , self.template_name, {'data': self.data} )


    def post(self , request ) :
        return render(request , self.template_name, {'data': self.data})

class ErrorView(View) :

    template_name = 'error_page.html'
    def get(self ,request ):
        return render(request , self.template_name, {})
    def post(self ,request ):
        return render(request , self.template_name, {})

























