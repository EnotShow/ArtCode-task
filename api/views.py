from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from api.models import Term, BrandTerm, Style
from api.serializers import TermSerializer, BrandTermSerializer, StyleSerializer


def test(request):
    return HttpResponse('work')


class TermsViewSet(viewsets.ModelViewSet):
    queryset = Term.objects.all()
    serializer_class = TermSerializer


class BrandTermsViewSet(viewsets.ModelViewSet):
    queryset = BrandTerm.objects.all()
    serializer_class = BrandTermSerializer


class StylesViewSet(viewsets.ModelViewSet):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer
