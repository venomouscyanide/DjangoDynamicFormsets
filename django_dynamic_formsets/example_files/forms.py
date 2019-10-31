from django import forms
from django.contrib.postgres.forms import SimpleArrayField, ValidationError
from django.core.validators import FileExtensionValidator
from material import Row, Layout


class ExampleForm1(forms.Form):
    array_of_elements = SimpleArrayField(
        forms.CharField(),
        label='Sample array field',
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'A Sample array input field'
        })
    )
    output_column_name = forms.CharField(
        required=True,
        label='Sample Char input',
        widget=forms.TextInput(attrs={
            'placeholder': 'A sample character input field'
        })
    )
    file_field = forms.FileField(
        label='File Upload Field Example',
        required=True,
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )

    layout = Layout(Row('array_of_elements'),
                    Row('output_column_name'),
                    Row('file_field'))
