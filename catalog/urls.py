# -*- encoding: utf-8 -*-
from django.urls import path
from catalog import views

urlpatterns = [

    path('categories', views.index_categories, name='categories.index'),
    path('categories/create', views.create_categories, name='categories.create'),
    path('categories/<int:id>/update', views.update_categories, name='categories.update'),
    path('categories/<int:id>/delete', views.delete_categories, name='categories.delete'),

    path('catalogs', views.index_catalogs, name='catalogs.index'),
    path('catalogs/create', views.create_catalogs, name='catalogs.create'),
    path('catalogs/<int:id>/update', views.update_catalogs, name='catalogs.update'),
    path('catalogs/<int:id>/delete', views.delete_catalogs, name='catalogs.delete'),
]
