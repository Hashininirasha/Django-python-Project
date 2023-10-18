from django.shortcuts import render

from .models import School, Class, Assessment_Areas, Answers, Awards, Student, Subject, Category, Summery


from .serializers import SchoolSerializer, ClassSerializer, Assessment_Areas_Serializer, AnswersSerializer, AwardsSerializer, StudentSerializer, SubjectSerializer, CategorySerializer, SummerySerializer
from rest_framework import viewsets



class SchoolView(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class ClassView(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class Assessment_Areas_View(viewsets.ModelViewSet):
    queryset = Assessment_Areas.objects.all()
    serializer_class = Assessment_Areas_Serializer
    
class AnswersView(viewsets.ModelViewSet):
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer
    
class AwardsView(viewsets.ModelViewSet):
    queryset = Awards.objects.all()
    serializer_class = AwardsSerializer
    
class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class SubjectView(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class SummeryView(viewsets.ModelViewSet):
    queryset = Summery.objects.all()
    serializer_class = SummerySerializer