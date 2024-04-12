from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import CuisineType
from .forms import CuisineTypeForm

class CuisineTypeListView(LoginRequiredMixin, ListView):
    model = CuisineType
    template_name = 'cuisine_types/cuisine_type_list.html'
    context_object_name = 'cuisine_types'

class CuisineTypeCreateView(LoginRequiredMixin, CreateView):
    model = CuisineType
    form_class = CuisineTypeForm
    template_name = 'cuisine_types/cuisine_type_form.html'
    success_url = '/cuisine-types/'

class CuisineTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = CuisineType
    form_class = CuisineTypeForm
    template_name = 'cuisine_types/cuisine_type_form.html'
    success_url = '/cuisine-types/'
