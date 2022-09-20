from django.views import generic
from django.urls import path, include


urlpatterns = [
    path('', generic.TemplateView.as_view(template_name='core/index.html'))
]
