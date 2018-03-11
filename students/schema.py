import graphene

from graphene_django.types import DjangoObjectType

from .models import Student, Course

class StudentType(DjangoObjectType):
  class Meta:
    model = Student

class CourseType(DjangoObjectType):
  class Meta:
    model = Course

class Query(object):
  student = graphene.Field(StudentType,
                            id = graphene.Int()
                            )
  all_students = graphene.List(StudentType)

  def resolve_student(self, info, **kwargs):
    id = kwargs.get('id')
    return Student.objects.get(pk=id)
    
  def resolve_all_students(self, info, **kwargs):
    return Student.objects.all()
