from django import forms
from .models import CuisineType

class CuisineTypeForm(forms.ModelForm):
    class Meta:
        model = CuisineType
        fields = ['name', 'description']
        labels = {
            'name': 'Name',
            'description': 'Description',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'style': 'resize: none;'}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if CuisineType.objects.filter(name=name).exists():
            self.add_error('name', 'A CuisineType with this name already exists.')
        return name
