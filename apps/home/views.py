# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import loader
from django.urls import reverse

from apps.home.forms import EntitiesForm
from apps.home.models import EntitiesModel


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def create_entities(request):
    context = {'segment' : 'entities'}
    form = EntitiesForm(request.POST or None)

    if form.is_valid():
        entities = form.save(commit=False)
        entities.user_id = request.user.id
        entities.save()

        return HttpResponseRedirect('/entities')

    context['form'] = form
    html_template = loader.get_template('entities/create.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def index_entities(request):
    context = {'segment' : 'entities'}
    context["dataset"] = EntitiesModel.objects.filter(user_id=request.user.id)
    html_template = loader.get_template('entities/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def update_entities(request, id):
    context ={'segment': 'entities'}
 
    obj = get_object_or_404(EntitiesModel, id = id)
    form = EntitiesForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/entities")
 
    context["form"] = form
 
    html_template = loader.get_template('entities/update.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def delete_entities(request, id):
    context ={'segment': 'entities'}
 
    obj = get_object_or_404(EntitiesModel, id = id)
 
 
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/entities")
 
    html_template = loader.get_template('entities/delete.html')
    return HttpResponse(html_template.render(context, request))