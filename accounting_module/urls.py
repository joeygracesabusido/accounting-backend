from django.urls import path
from .import views



urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('chartsofaccount-post/', views.post_chartofaccount, name="create-chartofaccount"),
    path('chartsofaccount-list/', views.chart_of_account_list, name="create-chartofaccount"),
    path('chartsofaccount-delete/<str:pk>', views.deleteCOA, name="delete-chartofaccount"),
   
]