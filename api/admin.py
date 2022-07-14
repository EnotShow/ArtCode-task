from django.contrib import admin

from .models import Term, BrandTerm, Style


@admin.register(Term)
class TermsAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(BrandTerm)
class BrandTermsAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Style)
class StylesAdmin(admin.ModelAdmin):
    list_display = ('name',)
