from django.views import generic
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "front-end/index.html"