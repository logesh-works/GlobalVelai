from rest_framework import serializers
from .models import CountryList,StateList,DegreeList,SkillList,FieldsList

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

