
from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signup,name='signup'),
    path("index",index,name="index"),
    path('registration',registration,name='registration'),
    path('signout',signout,name='signout'),
    path('admin_view',admin_view,name='admin_view'),
    path("home",HomeView,name="home"),
    path("Diabetes",Diabetes,name="diabetes"),
    path("Heart",Heart,name="heart"),
    path("Breast",Breast,name="breast"),
    path('consultation',consultation,name='consultation'),
    path('appointment',appointment,name='appointment'),
    path('add_doctor',add_doctor,name='add_doctor'),
    path('consultation_request',consultation_request,name='consultation_request'),
    path('consultation_delete',consultation_delete,name='consultation_delete'),
    path('doctor_list',doctor_list,name='doctor_list'),
    path("RedirectError",RedirectError,name="RedirectError"),


    path("chat_bot",chat_bot,name ="chat_bot"),
    path("Suggestion",Suggestion,name="Suggestion")
]
