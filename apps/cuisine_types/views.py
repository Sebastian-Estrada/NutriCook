from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.core.mixins import MessageMixin

from .models import CuisineType
from .forms import CuisineTypeForm

class CuisineTypeListView(LoginRequiredMixin, MessageMixin, ListView):
    model = CuisineType
    template_name = 'cuisine_types/cuisine_type_list.html'
    context_object_name = 'cuisine_types'

class CuisineTypeCreateView(LoginRequiredMixin, MessageMixin, CreateView):
    model = CuisineType
    form_class = CuisineTypeForm
    template_name = 'cuisine_types/cuisine_type_form.html'
    success_url = '/cuisine-types/'

class CuisineTypeUpdateView(LoginRequiredMixin, MessageMixin, UpdateView):
    model = CuisineType
    form_class = CuisineTypeForm
    template_name = 'cuisine_types/cuisine_type_form.html'
    success_url = '/cuisine-types/'
