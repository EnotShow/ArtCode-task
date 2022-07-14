from django.db import models
from django.urls import reverse


class Term(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class BrandTerm(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Style(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
