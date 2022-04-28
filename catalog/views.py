from cmath import log
from multiprocessing import context
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import loader

from catalog.form import CatalogsForm, CategoriesForm
from catalog.models import CatalogsModel, CategoriesModel

@login_required(login_url="/login/")
def create_categories(request):
    context = {'segment': 'catalog'}
    form = CategoriesForm(request.POST or None)

    if form.is_valid():
        categories = form.save(commit=False)
        categories.user_id = request.user.id
        categories.save()

        return HttpResponseRedirect('/categories')

    context['form'] = form
    html_template = loader.get_template('categories/create.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def index_categories(request):
    context = {'segment': 'catalog'}
    context['dataset'] = CategoriesModel.objects.filter(user_id=request.user.id)
    html_template = loader.get_template('categories/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def update_categories(request, id):
    context = {'segment': 'catalog'}

    obj = get_object_or_404(CategoriesModel, id=id)
    form = CategoriesForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/categories")

    context['form'] = form

    html_template = loader.get_template('categories/update.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def delete_categories(request, id):
    context = {'segment': 'catalog'}

    obj = get_object_or_404(CategoriesModel, id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/categories")

    html_template = loader.get_template('categories/delete.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def create_catalogs(request):
    context = {'segment': 'catalog'}
    form = CatalogsForm(request.POST or None, user=request.user)

    if form.is_valid():
        catalogs = form.save(commit=False)
        catalogs.user_id = request.user.id
        catalogs.save()

        return HttpResponseRedirect('/catalogs')

    context['form'] = form
    html_template = loader.get_template('catalogs/create.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def index_catalogs(request):
    context = {'segment': 'catalog'}
    context["dataset"] = CatalogsModel.objects.filter(user_id=request.user.id)

    html_template = loader.get_template('catalogs/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def update_catalogs(request, id):
    context = {'segment': 'catalog'}
    
    obj = get_object_or_404(CatalogsModel, id=id)
    form = CatalogsForm(request.POST or None, user=request.user, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/catalogs")

    context["form"] = form

    html_template = loader.get_template('catalogs/update.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def delete_catalogs(request, id):
    context = {'segment': 'catalog'}

    obj = get_object_or_404(CatalogsModel, id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/catalogs")

    html_template = loader.get_template('catalogs/delete.html')
    return HttpResponse(html_template.render(context, request))