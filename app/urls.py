from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("year/",views.year,name="year"),
    path("month/",views.month,name="month"),

]