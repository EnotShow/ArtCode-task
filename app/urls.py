from django.urls import path
from .views import app_view

urlpatterns = [
    path('', app_view, name='home'),
    path(f"s-<slug:selected_term>/b-<slug:selected_brand>/st-<slug:selected_style>", app_view)
]
