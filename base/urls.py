from django.urls import path
from .views import (
    UserListView,
    CountryListCreateView, CountryDetailView,
    StateListCreateView, StateDetailView,
    DegreeListCreateView, DegreeDetailView,
    FieldsListCreateView, FieldsDetailView,
    SkillListCreateView, SkillDetailView,
    ApplicantListCreateView , ApplicantDetailView,
    CompanyProfileListCreateView,CompanyProfileDetailView,
    WorkDetailsListCreateView,WorkDetailsDetailView,
    AwardsDetailsListCreateView,AwardsDetailsDetailView,
    EducationDetailsListCreateView,EducationDetailsDetailView,
    PreferenceDetailsListCreateView,PreferenceDetailsDetailView,
    CertificationDetailsListCreateView,CertificationDetailsDetailView
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
    path('applicants/', ApplicantListCreateView.as_view(), name='applicant-list-create'),
    path('applicants/<int:pk>/', ApplicantDetailView.as_view(), name='applicant-detail'),
    path('CompanyProfile/', CompanyProfileListCreateView.as_view(), name='CompanyProfile-list-create'),
    path('CompanyProfile/<int:pk>/', CompanyProfileDetailView.as_view(), name='CompanyProfilet-detail'),
    path("user/",UserListView.as_view(),name="user"),
    path('work-details/', WorkDetailsListCreateView.as_view(), name='work-details-list-create'),
    path('work-details/<int:pk>/', WorkDetailsDetailView.as_view(), name='work-details-detail'),
    path('awards-details/', AwardsDetailsListCreateView.as_view(), name='awards-details-list-create'),
    path('awards-details/<int:pk>/', AwardsDetailsDetailView.as_view(), name='awards-details-detail'),
    path('education-details/', EducationDetailsListCreateView.as_view(), name='education-details-list-create'),
    path('education-details/<int:pk>/', EducationDetailsDetailView.as_view(), name='education-details-detail'),
    path('preference-details/', PreferenceDetailsListCreateView.as_view(), name='preference-details-list-create'),
    path('preference-details/<int:pk>/', PreferenceDetailsDetailView.as_view(), name='preference-details-detail'),
    path('certification-details/', CertificationDetailsListCreateView.as_view(), name='certification-details-list-create'),
    path('certification-details/<int:pk>/', CertificationDetailsDetailView.as_view(), name='certification-details-detail')
]