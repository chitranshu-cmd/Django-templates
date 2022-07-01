from django.urls import path,include
from  . import views
 
urlpatterns = [
    #path('',views.base,name="base"),'''
    path('',views.index,name="index"),
    path('sign/',views.sign,name="sign"),
    path('login/',views.login,name="login"),
    path('about/',views.about,name="about")

     
]
    