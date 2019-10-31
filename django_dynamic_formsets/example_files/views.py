from django.forms import formset_factory
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from django_dynamic_formsets.example_files.forms import ExampleForm1


class Example1(View):
    EXAMPLE_1_PREFIX = "example_1"

    def get(self, request):
        context = self._generate_context()
        return render(request, "examples/example_1.html", context)

    def post(self, request):
        print("There is no backend handled. This project simply aims at showcasing dynamic formsets in Django!")
        return HttpResponse('Success', status=200)

    def _generate_context(self):
        example_1_formset = formset_factory(ExampleForm1, extra=1, can_delete=True)
        context = {"example_1_formset": example_1_formset}
        return context
