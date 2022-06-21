from django.shortcuts import render,redirect, HttpResponseRedirect
from django.views.generic import View, TemplateView
from .forms import  CategoriesForm
from .models import *
# Create your views here.
def dashboard(request):

    return render(request, 'dashboard.html', {})

def addCategories(request):
    if request.method == "POST":
        categoriesForm = CategoriesForm(request.POST)
        if categoriesForm.is_valid():
            nm = categoriesForm.cleaned_data['name']
            categoriesAdded = Categories(name=nm)
            categoriesAdded.save()
            categoriesForm = CategoriesForm ()
    else:
        categoriesForm = CategoriesForm ()
    cats = Categories.objects.all()
    return render(request, 'categories.html',{'categoriesform': categoriesForm, 'cats':cats})

def deleteCategories(request, id):
    if request.method == "POST":
        categoryData = Categories.objects.get(pk=id)
        categoryData.delete()
    return redirect("/")

def updateCategories(request, id):
    if request.method == "POST":
        catagories = Categories.objects.get(pk=id)
        updateData = CategoriesForm(request.POST, instance = catagories)
        if updateData.is_valid():
            updateData.save()
    else:
        catagories = Categories.objects.get(pk=id)
        updateData = CategoriesForm(instance = catagories)


    # return HttpResponseRedirect('/')
    return render(request, 'updateCatagories.html',{'updateData':updateData})

def projects(request):
    return render(request, 'projects.html', {})

class UserViews(TemplateView):
    template_name = "users.html"