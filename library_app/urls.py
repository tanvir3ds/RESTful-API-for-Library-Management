
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name= 'home'),
    path('registration',views.registration, name= 'registration'  ),
    path('login',views.login, name= 'login'  ),
    path('logout',views.logout, name= 'logout'  ),
    path('showbook/<id>/', views.ShowBook, name='showbook' ),
    path('loanbook', views.LoanBook, name='loanbook' ),
    path('profile', views.Profile, name='profile' ),
    path('uploadimage/<id>/', views.UploadImage, name='upload' ),
    

    

]
