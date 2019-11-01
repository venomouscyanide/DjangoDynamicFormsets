from django.contrib import messages
from django.forms import formset_factory
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from django_dynamic_formsets.example_files.forms import ExampleForm1, ExampleForm2


class Example1(View):
    EXAMPLE_1_PREFIX = "example_1_formset"

    def get(self, request):
        context = self._generate_context()
        return render(request, "examples/example_1.html", context)

    def post(self, request):
        print("Refer to the second example on how to handle backend!")
        return HttpResponse('Success', status=200)

    def _generate_context(self):
        example_1_formset = formset_factory(ExampleForm1, extra=1)(prefix=self.EXAMPLE_1_PREFIX)
        context = {self.EXAMPLE_1_PREFIX: example_1_formset}
        return context


class Example2(View):
    EXAMPLE_2_PREFIX = "example_2_formset"

    def get(self, request):
        context = self._generate_context()
        return render(request, "examples/example_2.html", context)

    def post(self, request):
        example_2_formset = self._get_formset()(data=request.POST, prefix=self.EXAMPLE_2_PREFIX)

        if example_2_formset.is_valid():
            for form in example_2_formset:
                form.save()
            messages.success(request, "Successfully saved the formset!")
            context = self._generate_context()
            return render(request, "examples/example_2.html", context)
        else:
            print("Invalid data in the form!")

        context = self._generate_context(example_2_formset)
        return render(request, "examples/example_2.html", context)

    def _generate_context(self, example_2_formset=None):
        example_2_formset = self._get_formset()(
            prefix=self.EXAMPLE_2_PREFIX) if not example_2_formset else example_2_formset
        context = {self.EXAMPLE_2_PREFIX: example_2_formset}
        return context

    def _get_formset(self):
        return formset_factory(ExampleForm2, extra=1)
