from django.contrib.auth.models import User
from rest_framework import serializers
from .models import CountryList,StateList,DegreeList,SkillList,FieldsList,Applicant,CompanyProfile,WorkDetails,AwardsDetails,EducationDetails,PreferenceDetails,CertificationDetails

class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryList
        fields = '__all__'
class StateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateList
        fields = '__all__'
class DegreeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DegreeList
        fields = '__all__'
class SkillListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillList
        fields = '__all__'
class FieldsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldsList
        fields = '__all__'

class ApplicantSerilalizer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'

class CompanyProfileSerilalizer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = '__all__'

class UserSerilalizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password',"is_superuser"]

class WorkDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkDetails
        fields = '__all__'

class AwardsDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardsDetails
        fields = '__all__'

class EducationDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationDetails
        fields = '__all__'

class PreferenceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreferenceDetails
        fields = '__all__'

class CertificationDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificationDetails
        fields = '__all__'

    

