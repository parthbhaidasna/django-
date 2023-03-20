from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
     path('managerregister/',ManagerRegisterView.as_view(),name='managerregister'),
  path('developerregister/',DeveloperRegisterView.as_view(),name='developerregister'),
    path('teamleaderregister/',TeamLeaderRegisterView.as_view(),name='developerregister'),
    path('testerregister/',TesterRegisterView.as_view(),name='testerregister'),
     path('login/',UserLoginView.as_view(),name='login'),  
]
