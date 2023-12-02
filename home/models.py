from ckeditor.fields import RichTextField

from django.db import models


class Header(models.Model):
    title = RichTextField(max_length=50)
    paragraph = RichTextField(max_length=200)
    img = models.ImageField(upload_to="uploads/")


class ProvideServices(models.Model):
    svg = models.ImageField(upload_to="uploads/")
    title = RichTextField(max_length=50)
    text = RichTextField(max_length=200)


class WorkExperience(models.Model):
    title = RichTextField(max_length=50)
    description = RichTextField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    link = models.TextField(max_length=100, null=True, blank=True)


class Education(models.Model):
    title = RichTextField(max_length=50)
    description = RichTextField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    link = models.TextField(max_length=100, null=True, blank=True)


class FreelanceClients(models.Model):
    logo = models.ImageField(upload_to="uploads/")


class Skills(models.Model):
    text = RichTextField(max_length=30)


class Tools(models.Model):
    svg = models.ImageField(upload_to="uploads/", validators=[])


class Stats(models.Model):
    projectsCompleted = models.IntegerField(default=0)
    designAwards = models.IntegerField(default=0)
    yearsExperience = models.IntegerField(default=0)
    happyClients = models.IntegerField(default=0)


class ClientsFeedbacks(models.Model):
    text = RichTextField(max_length=200)
    img = models.ImageField(upload_to="uploads/")
    name = RichTextField(max_length=100)
