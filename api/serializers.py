from rest_framework import serializers

from api.models import Term, BrandTerm, Style


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ['name', 'slug']


class BrandTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandTerm
        fields = ['name', 'slug']


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = ['name', 'slug']

