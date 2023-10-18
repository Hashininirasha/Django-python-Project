from django.db import models

  
class School(models.Model):
    School_Id = models.CharField(max_length=100, null=False, blank=False, primary_key=True)
    Sch_Name=models.CharField(max_length=200, null=False, blank=False)
    
    def __str__(self):
        return self.School_Id
    
class Class(models.Model):
    Class_Id = models.CharField(max_length=100, null=False, blank=False, primary_key=True)
    Class = models.CharField(max_length=200, null=False, blank=False)

    
    def __str__(self):
        return self.Class_Id
    
class Assessment_Areas(models.Model):
    Assessment_Areas_Id = models.CharField(max_length=100, null=False, blank=False, primary_key=True)
    Assessment_Area = models.CharField(max_length=200, null=False, blank=False)

    
    def __str__(self):
        return self.Assessment_Areas_Id
    
class Answers(models.Model):
    Answer_Id = models.CharField(max_length=100, null=False, blank=False, primary_key=True)
    Answer = models.CharField(max_length=50, null=False, blank=False)

    
    def __str__(self):
        return self.Answer_Id
    
class Awards(models.Model):
    Award_Id= models.CharField(max_length=100, null=False, blank=False, primary_key=True)
    Award = models.CharField(max_length=100, null=False, blank=False)

    
    def __str__(self):
        return self.Award_Id
    
class Student(models.Model):
    Student_Id= models.CharField(max_length=100, null=False, blank=False, primary_key=True)
    Fullname = models.CharField(max_length=200, null=False, blank=False)

    
    def __str__(self):
        return self.Student_Id
    
class Subject(models.Model):
    Subject_Id= models.CharField(max_length=100, null=False, blank=False, primary_key=True)
    Subject = models.CharField(max_length=200, null=False, blank=False)
    Subject_score = models.FloatField(null=False, blank=False)
    
    def __str__(self):
        return self.Subject_Id
    
class Category(models.Model):
    Category_Id= models.CharField(max_length=100, null=False, blank=False, primary_key=True)
    Category = models.CharField(max_length=200, null=False, blank=False)

    
    def __str__(self):
        return self.Category_Id
    
class Summery(models.Model):
    School_Id= models.ForeignKey(School, on_delete=models.CASCADE)
    sydney_participants=models.IntegerField(null=False, blank=False)
    sydney_percentile=models.IntegerField(null=False, blank=False)
    Assessment_areas_Id=models.ForeignKey(Assessment_Areas, on_delete=models.CASCADE)
    Award_Id = models.ForeignKey(Awards, on_delete=models.CASCADE)
    Class_Id = models.ForeignKey(Class, on_delete=models.CASCADE)
    correct_answer_percentage_per_class=models.FloatField(null=False, blank=False)
    Correct_Answer = models.CharField(max_length=100, null=False, blank=False)
    Student_Id= models.ForeignKey(Student, on_delete=models.CASCADE)
    participant = models.IntegerField(null=False, blank=False)
    student_score = models.FloatField(null=False, blank=False)
    Subject_Id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Category_Id = models.ForeignKey(Category, on_delete=models.CASCADE)
    Year_level_name = models.IntegerField(null=False, blank=False)
    Answer_Id = models.ForeignKey(Answers, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.Category_Id