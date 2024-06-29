from   django.urls import path
from .views import HomeView , DetailView , GuideView , ErrorView


app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view() , name='home'),
    path('<int:page>/', HomeView.as_view(), name='home') ,
    path('detail/<int:id>/', DetailView.as_view(), name='detail') ,
    path('guide/', GuideView.as_view() , name='guide' ) ,
    path('error/', ErrorView.as_view(), name='error')

]