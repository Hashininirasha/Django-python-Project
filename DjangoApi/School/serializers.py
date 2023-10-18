from rest_framework import serializers

from .models import School, Class, Assessment_Areas, Answers, Awards, Student, Subject, Category, Summery

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
        
class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'
        
class Assessment_Areas_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment_Areas
        fields = '__all__'
        
class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = '__all__'
        
class AwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awards
        fields = '__all__'
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class SummerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summery
        fields = '__all__'