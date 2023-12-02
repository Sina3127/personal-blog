from django.shortcuts import render
from django.views.generic import TemplateView

from home.models import Header, ProvideServices, WorkExperience, Education, Skills, Tools, Stats, ClientsFeedbacks, \
    FreelanceClients


class Home(TemplateView):
    template_name = "home/index.html"

    def get(self, request):
        header = Header.objects.last()
        provideServices = ProvideServices.objects.all()
        workExperience = WorkExperience.objects.all()
        education = Education.objects.all()
        freelanceClients = FreelanceClients.objects.all()
        skills = Skills.objects.all()
        tools = Tools.objects.all()
        stats = Stats.objects.last()
        clientsFeedbacks = ClientsFeedbacks.objects.all()

        context = {
            'header': header,
            'provideServices': provideServices,
            'workExperience': workExperience,
            'education': education,
            'freelanceClients' : freelanceClients,
            'skills': skills,
            'tools': tools,
            'stats': stats,
            'clientsFeedbacks': clientsFeedbacks,
        }

        return render(request, "home/index.html", context)