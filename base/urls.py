from django.urls import path
from .views import (
    CountryListCreateView, CountryDetailView,
    StateListCreateView, StateDetailView,
    DegreeListCreateView, DegreeDetailView,
    FieldsListCreateView, FieldsDetailView,
    SkillListCreateView, SkillDetailView
)
app_name = "base"
urlpatterns = [
    path('countries/', CountryListCreateView.as_view(), name='country-list-create'),
    path('countries/<int:pk>/', CountryDetailView.as_view(), name='country-detail'),
    path('states/', StateListCreateView.as_view(), name='state-list-create'),
    path('states/<int:pk>/', StateDetailView.as_view(), name='state-detail'),
    path('degrees/', DegreeListCreateView.as_view(), name='degree-list-create'),
    path('degrees/<int:pk>/', DegreeDetailView.as_view(), name='degree-detail'),
    path('fields/', FieldsListCreateView.as_view(), name='fields-list-create'),
    path('fields/<int:pk>/', FieldsDetailView.as_view(), name='fields-detail'),
    path('skills/', SkillListCreateView.as_view(), name='skill-list-create'),
    path('skills/<int:pk>/', SkillDetailView.as_view(), name='skill-detail'),
]