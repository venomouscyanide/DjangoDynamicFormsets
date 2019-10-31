from django.urls import path

from django_dynamic_formsets.example_files.views import Example1

urlpatterns = [
    path('', Example1.as_view(), name='example_1')
]
