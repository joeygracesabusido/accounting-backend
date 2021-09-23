from django.urls import path
from . import views
from . views import NoteList, NoteListDetails


urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('notes/', views.getNotes, name="notes"),
    path('notes/<str:pk>/update', views.updateNote, name="updatenote"),
    # path('search/', NoteListDetails.as_view(), name="listnoteDetail"),
    path('posts/<str:pk>/', NoteList.as_view(), name="listnote"),
    path('search/<str:pk>/', views.searchNote, name="Searchnote"),
    path('note/<str:pk>/delete', views.deleteNote, name="delete-note"),
    path('note/<str:pk>/', views.getNote, name="note"),
    path('notes-post/', views.post_data, name="post-data"),
]
 