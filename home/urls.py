from django.urls import path
from .views import HomeView , RecordTimeView , ShowDetailView



app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='home'  ) ,
    path('record/', RecordTimeView.as_view(), name='record_time') ,
    path('show_detail/<int:id>/', ShowDetailView.as_view(), name='detail_record') ,
]