from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.forms import ModelForm

from django.shortcuts import render, redirect, get_object_or_404

from django.shortcuts import render, redirect
from .models import Certification
from .forms import CertForm
from django.contrib import messages

from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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
    return render(request,'home.html')


def create(request):
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


def modify(request):
    return render(request,'modify.html', {"test": "hello"})


class CertificationForm(ModelForm):
    class Meta:
        model = Certification
        fields = ['first_name', 'last_name', 'ssn', 'returning_or_new_hire', 'title_position', 'current_assignment', 'subject_grade', 'certification_status', 'nys_cert_area', 'cert_type', 'expiration_date', 'current_comment', 'comments_from_last_wksh', 'las', 'ats_w', 'cst', 'cst_subject', 'eas', 'ata']

def teacher_list(request, template_name='teacher_list.html'):
    teacher = Certification.objects.all()
    data = {}
    data['object_list'] = teacher
    return render(request, template_name, data)

def teacher_view(request, pk, template_name='teacher_detail.html'):
    teacher= get_object_or_404(Certification, pk=pk)    
    return render(request, template_name, {'object': teacher})

def teacher_create(request, template_name='teacher_form.html'):
    form = CertificationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('teacher_list')
    return render(request, template_name, {'form':form})

def teacher_update(request, pk, template_name='teacher_form.html'):
    teacher= get_object_or_404(Certification, pk=pk)
    form = CertificationForm(request.POST or None, instance=teacher)
    if form.is_valid():
        form.save()
        return redirect('teacher_list')
    return render(request, template_name, {'form':form})

def teacher_delete(request, pk, template_name='teacher_confirm_delete.html'):
    teacher= get_object_or_404(Certification, pk=pk)    
    if request.method=='POST':
        teacher.delete()
        return redirect('teacher_list')
    return render(request, template_name, {'object': teacher})