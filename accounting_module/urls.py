from django.urls import path
from .import views



urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('chartsofaccount-post/', views.post_chartofaccount, name="create-chartofaccount"),
    path('coa/<str:pk>/', views.getChartofAccount, name="get-coa"),
    path('chartsofaccount-list/', views.chart_of_account_list, name="create-chartofaccount"),
    path('chartsofaccount-delete/<str:pk>', views.deleteCOA, name="delete-chartofaccount"),
    path('coa-update/<str:pk>', views.update_coa, name="update-coa"),
    path('journal-post/', views.post_journalEntry, name="post-journal"),
   
]