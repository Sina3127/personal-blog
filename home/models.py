from django.db import models

from django.db import models


class Header(models.Model):
    title = models.CharField(max_length=50)
    paragraph = models.TextField(max_length=200)
    img = models.ImageField(upload_to="uploads")


class ProvideServices(models.Model):
    # svg =
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=200)


class WorkExperience(models.Model):
    title = models.CharField(max_length=50)
    duration = models.TextField(max_length=50)


class Education(models.Model):
    title = models.CharField(max_length=50)
    duration = models.TextField(max_length=50)


# class FreelanceClients(models.models):
#      svg =

class Skills(models.Model):
    text = models.CharField(max_length=30)


# class tools(models.Model):
#     svg =

class Stats(models.Model):
    projectsCompleted = models.IntegerField(default=0)
    designAwards = models.IntegerField(default=0)
    YearsExperience = models.IntegerField(default=0)
    happyClients = models.IntegerField(default=0)


class ClientsFeedbacks(models.Model):
    text = models.CharField(max_length=200)
    img = models.ImageField(upload_to="uploads")
