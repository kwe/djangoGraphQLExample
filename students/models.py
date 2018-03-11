from django.db import models

class Course(models.Model):
  title = models.CharField(max_length=200)

  def __str__(self):
    return self.title

class Student(models.Model):
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200, default="None")

  student_id = models.IntegerField(default=0)
  course = models.ForeignKey(Course, on_delete= models.CASCADE)

  def __str__(self):
    return self.first_name + ' ' + self.last_name



