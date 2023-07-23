from django.urls import path

from . import views

urlpatterns = [
    path('', views.teacher_list, name='teacher_list'),
    path('view/<int:pk>', views.teacher_view, name='teacher_view'),
    path('new', views.teacher_create, name='teacher_new'),
    path('view/<int:pk>', views.teacher_view, name='teacher_view'),
    path('edit/<int:pk>', views.teacher_update, name='teacher_edit'),
    path('delete/<int:pk>', views.teacher_delete, name='teacher_delete'),
]