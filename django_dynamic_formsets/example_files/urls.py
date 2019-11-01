from django.urls import path

from django_dynamic_formsets.example_files.views import Example1, Example2

urlpatterns = [
    path('example1/', Example1.as_view(), name='example_1'),
    path('example2/', Example2.as_view(), name='example_2')
]
