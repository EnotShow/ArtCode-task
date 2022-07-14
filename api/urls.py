from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api.views import TermsViewSet, BrandTermsViewSet, StylesViewSet, test

router = routers.DefaultRouter()
router.register(r'terms', TermsViewSet)
router.register(r'brand_terms', BrandTermsViewSet)
router.register(r'styles', StylesViewSet)

urlpatterns = [
    path('test/', test),
    path('', include(router.urls))
]
