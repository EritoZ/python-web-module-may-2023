from django.urls import path, include

from plantsApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', include(
        [path('create/', views.profile_create, name='profile create'),
         path('details/', views.profile_details, name='profile details'),
         path('edit/', views.profile_edit, name='profile edit'),
         path('delete/', views.profile_delete, name='profile delete'),
         ])),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('create/', views.plant_create, name='plant create'),
    path('details/<int:plant_id>/', views.plant_details, name='plant details'),
    path('edit/<int:plant_id>/', views.plant_edit, name='plant edit'),
    path('delete/<int:plant_id>/', views.plant_delete, name='plant delete'),
]
