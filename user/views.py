from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from user.forms import AddForm
# Create your views here.

def home(request):
    return render(request, 'registration/home.html')

def logout_page(request):
    return render(request, 'registration/logout_page.html')

def singup(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = AddForm()
    return render(request, 'registration/singup.html', {'form':form})