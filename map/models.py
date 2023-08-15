from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager,User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Usermapping(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    is_pwd =models.BooleanField(default=False)
    is_traffic=models.BooleanField(default=False)

    def __str__(self):

        return self.user


class traffic(models.Model):
    tname = models.CharField(max_length=150,null=False,blank=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    tphone =models.IntegerField(null=False,blank=False)
    tplace = models.CharField(max_length=150,null=False,blank=False)
    tissue = models.CharField(max_length=150,null=False,blank=False)
    timage=models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class road(models.Model):
    name = models.CharField(max_length=150,null=False,blank=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone =models.IntegerField(null=False,blank=False)
    place = models.CharField(max_length=150,null=False,blank=False)
    issue = models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)









# class User(AbstractUser):
#     class Role(models.TextChoices):
#         ADMIN = "ADMIN", "Admin"
#         STUDENT = "STUDENT", "Student"
#         TEACHER = "TEACHER", "Teacher"

#     base_role = Role.STUDENT

#     role = models.CharField(max_length=50, choices=Role.choices)

#     def save(self, *args, **kwargs):
#         if not self.pk:
#             self.role = self.base_role
#             return super().save(*args, **kwargs)


# class StudentManager(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(role=User.Role.STUDENT)


# class Student(User):

#     base_role = User.Role.STUDENT

#     student = StudentManager()

#     class Meta:
#         proxy = True

#     def welcome(self):
#         return "Only for students"





# class TeacherManager(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(role=User.Role.TEACHER)


# class Teacher(User):

#     base_role = User.Role.TEACHER

#     teacher = TeacherManager()

#     class Meta:
#         proxy = True

#     def welcome(self):
#         return "Only for teachers"





# # Create your models here.
