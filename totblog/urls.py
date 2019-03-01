from django.urls import path
from . import views

app_name = 'totblog'
#URLS from here

urlpatterns = [
    path('', views.PostView.as_view(), name = 'postview')
]