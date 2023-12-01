from django.contrib import admin
from .models import Header, ProvideServices, WorkExperience, Education, Skills, Tools, Stats, ClientsFeedbacks, \
    FreelanceClients

admin.site.register(Header)
admin.site.register(ProvideServices)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Skills)
admin.site.register(Tools)
admin.site.register(Stats)
admin.site.register(ClientsFeedbacks)
admin.site.register(FreelanceClients)