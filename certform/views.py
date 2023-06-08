from django.shortcuts import render
from django.contrib import messages
# Create your views here.

from django.shortcuts import render, redirect
from .models import Certification
from .forms import CertForm
from django.contrib import messages

# Create your views here.
# def homepage(request):
#     form = CertForm(request.POST)
#     context = {'form': form}
    
#     if request.method == 'POST':
#         if form.is_valid():
#             try:
#                 # form.save(commit=False)
#                 form.save()
#                 form = CertForm()
#                 context = {'form': form}
#                 # return render(request,'certification.html', {'form': form})
#             except Exception as e:
#                 print(e)
#     return render(request,'certification.html', context)

def homepage(request):
    if request.method == 'POST':
        form = CertForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')
            redirect('/')
    form = CertForm()
    # showcomment = Certification.objects.filter(id=id)
    context = {'form': form}
    return render(request,'certification.html', context)