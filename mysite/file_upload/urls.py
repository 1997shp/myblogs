from django.urls import path
from . import views


#start with blog
urlpatterns = [
    path('',views.model_form_upload,name = 'model_form_upload'),


]