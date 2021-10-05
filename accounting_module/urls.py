from django.urls import path
from .import views
from . views import test_api, testApi



urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('chartsofaccount-post/', views.post_chartofaccount, name="create-chartofaccount"),
    path('coa/<str:pk>/', views.getChartofAccount, name="get-coa"),
    path('chartsofaccount-list/', views.chart_of_account_list, name="create-chartofaccount"),
    path('chartsofaccount-delete/<str:pk>', views.deleteCOA, name="delete-chartofaccount"),
    path('coa-update/<str:pk>', views.update_coa, name="update-coa"),
    path('journal-post2/', views.testApi, name="journla-post2"),
    path('journal-post/', views.post_journalEntry, name="post-journal"),
    path('journal-list/', views.journalEntry_list, name="list-journal"),
   
]