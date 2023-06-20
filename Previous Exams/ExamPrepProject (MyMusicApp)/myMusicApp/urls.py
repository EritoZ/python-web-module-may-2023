from django.urls import path, include

from myMusicApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('album/', include([
        path('add/', views.album_add, name='album add'),
        path('details/<int:id>/', views.album_details, name='album details'),
        path('edit/<int:id>/', views.album_edit, name='album edit'),
        path('delete/<int:id>/', views.album_delete, name='album delete'),
    ])),
    path('profile/', include([
        path('details/', views.profile_details, name='profile details'),
        path('delete/', views.profile_delete, name='profile delete'),
    ]))
]
