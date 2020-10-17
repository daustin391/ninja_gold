from django.urls import path
from gold import views

urlpatterns = [path("", views.index), path("process_money", views.process)]
