"""nutricook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include

from apps.users.views import Login

urlpatterns = [
    path('', Login.as_view(), name="login"),
    path('select2/', include('django_select2.urls')),

    path('users/', include('apps.users.urls', namespace="users")),
    path('recipes/', include('apps.recipes.urls', namespace="recipes")),
    path('meals/', include('apps.meals.urls', namespace="meals")),
    path('meal-types/', include('apps.meal_types.urls', namespace="meal_types")),
    path('ingredients/', include('apps.ingredients.urls', namespace="ingredients")),
    path('cuisine-types/', include('apps.cuisine_types.urls', namespace="cuisine_types")),
    path('dashboards/', include('apps.dashboards.urls', namespace="dashboards")),
    path('planner/', include('apps.meal_planner.urls', namespace="planner")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
