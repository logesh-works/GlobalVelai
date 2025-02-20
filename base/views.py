from django.contrib.auth.models import User
from rest_framework import generics
from .models import CountryList,StateList,DegreeList,SkillList,FieldsList,Applicant,CompanyProfile,WorkDetails,AwardsDetails,EducationDetails,PreferenceDetails,CertificationDetails
from .serializers import CountryListSerializer, StateListSerializer, DegreeListSerializer, FieldsListSerializer, SkillListSerializer,ApplicantSerilalizer,CompanyProfileSerilalizer,UserSerilalizer,WorkDetailsSerializer,AwardsDetailsSerializer,EducationDetailsSerializer,PreferenceDetailsSerializer,CertificationDetailsSerializer

class CountryListCreateView(generics.ListCreateAPIView):
    queryset = CountryList.objects.all()
    serializer_class = CountryListSerializer

class CountryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CountryList.objects.all()
    serializer_class = CountryListSerializer

class StateListCreateView(generics.ListCreateAPIView):
    queryset = StateList.objects.all()
    serializer_class = StateListSerializer

class StateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StateList.objects.all()
    serializer_class = StateListSerializer

class DegreeListCreateView(generics.ListCreateAPIView):
    queryset = DegreeList.objects.all()
    serializer_class = DegreeListSerializer

class DegreeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DegreeList.objects.all()
    serializer_class = DegreeListSerializer

class FieldsListCreateView(generics.ListCreateAPIView):
    queryset = FieldsList.objects.all()
    serializer_class = FieldsListSerializer

class FieldsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FieldsList.objects.all()
    serializer_class = FieldsListSerializer

class SkillListCreateView(generics.ListCreateAPIView):
    queryset = SkillList.objects.all()
    serializer_class = SkillListSerializer

class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SkillList.objects.all()
    serializer_class = SkillListSerializer

class ApplicantListCreateView(generics.ListCreateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerilalizer

class ApplicantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerilalizer

class CompanyProfileListCreateView(generics.ListCreateAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerilalizer

class CompanyProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerilalizer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerilalizer

class WorkDetailsListCreateView(generics.ListCreateAPIView):
    queryset = WorkDetails.objects.all()
    serializer_class = WorkDetailsSerializer

class WorkDetailsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkDetails.objects.all()
    serializer_class = WorkDetailsSerializer

class AwardsDetailsListCreateView(generics.ListCreateAPIView):
    queryset = AwardsDetails.objects.all()
    serializer_class = AwardsDetailsSerializer

class AwardsDetailsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AwardsDetails.objects.all()
    serializer_class = AwardsDetailsSerializer

class EducationDetailsListCreateView(generics.ListCreateAPIView):
    queryset = EducationDetails.objects.all()
    serializer_class = EducationDetailsSerializer

class EducationDetailsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EducationDetails.objects.all()
    serializer_class = EducationDetailsSerializer

class PreferenceDetailsListCreateView(generics.ListCreateAPIView):
    queryset = PreferenceDetails.objects.all()
    serializer_class = PreferenceDetailsSerializer

class PreferenceDetailsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PreferenceDetails.objects.all()
    serializer_class = PreferenceDetailsSerializer

class CertificationDetailsListCreateView(generics.ListCreateAPIView):
    queryset = CertificationDetails.objects.all()
    serializer_class = CertificationDetailsSerializer

class CertificationDetailsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CertificationDetails.objects.all()
    serializer_class = CertificationDetailsSerializer


