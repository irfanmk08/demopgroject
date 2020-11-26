from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=200)
    address=models.TextField(max_length=200)
    age=models.IntegerField()

    class Meta:
        verbose_name_plural="Student_Details"

    def __str__(self):
        return self.name
# # Create your models here.
class Emp(models.Model):
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Username = models.CharField(max_length=200)
    Address = models.TextField(max_length=200)
    Age = models.IntegerField()
    Gender_Choices=(('M','Male'),('F','Female'))
    gender = models.TextField(choices=Gender_Choices,default='NA')
    password=models.CharField(max_length=50,default='NA')
    Confirmpassword=models.CharField(max_length=50,default='NA')

    class Meta:
        verbose_name_plural="Employee_Details"

    def __str__(self):
        return self.First_Name

class newstudent(models.Model):
    name = models.CharField(max_length=200)
    Age = models.IntegerField(max_length=200)
    Address = models.TextField(max_length=200)
    list1 = (('Male', 'Male'), ('Female', 'Female'))
    gender = models.TextField(choices=list1)
    FRUIT_CHOICES = [
        ('Orange', 'Orange'),
        ('Apple', 'Apple'),
        ('Grape', 'Grape'),
        ('Kiwi', 'Kiwi')
    ]
    favorite_fruit=models.TextField(choices=FRUIT_CHOICES)
    email=models.EmailField(max_length=200)
    fileupload=models.FileField(upload_to="Documents",default="NA")

    class Meta:
        verbose_name_plural="New_Studentdetails"

    def __str__(self):
        return self.name



