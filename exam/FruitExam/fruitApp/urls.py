from django.urls import path, include

from fruitApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.fruit_create, name='fruit create'),
    path('<int:fruit_id>/', include([
        path('details/', views.fruit_details, name='fruit details'),
        path('edit/', views.fruit_edit, name='fruit edit'),
        path('delete/', views.fruit_delete, name='fruit delete'),
    ])),
    path('profile/', include([
        path('details/', views.profile_details, name='profile details'),
        path('create/', views.profile_create, name='profile create'),
        path('edit/', views.profile_edit, name='profile edit'),
        path('delete/', views.profile_delete, name='profile delete'),
    ]))
]
