from django.urls import path
from .import views



urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('chartsofaccount-post/', views.post_chartofaccount, name="create-chartofaccount"),
   
]