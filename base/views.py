from rest_framework import generics
from .models import CountryList,StateList,DegreeList,SkillList,FieldsList
from .serializers import CountryListSerializer, StateListSerializer, DegreeListSerializer, FieldsListSerializer, SkillListSerializer

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
