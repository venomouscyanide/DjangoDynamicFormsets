from django import forms
from django.contrib.postgres.forms import SimpleArrayField
from material import Row, Layout

from django_dynamic_formsets.users.models import Example2Model


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

    layout = Layout(Row('array_of_elements', 'output_column_name'),
                    Row('file_field'))


class ExampleForm2(forms.ModelForm):
    class Meta:
        model = Example2Model
        fields = ('name', 'email', 'address', 'phone_number')
        help_texts = {
            'name': 'Your name',
            'email': 'Your email address',
            'address': 'Your Address',
            'phone_number': 'Your Phone Number'
        }
        layout = Layout(Row('name'),
                        Row('email'),
                        Row('address'),
                        Row('phone_number'))
