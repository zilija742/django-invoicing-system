# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    path('entities', views.index_entities, name='entities.index'),
    path('entities/create', views.create_entities, name='entities.create'),
    path('entities/<int:id>/update', views.update_entities, name='entities.update'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
