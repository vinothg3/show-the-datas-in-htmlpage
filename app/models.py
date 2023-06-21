from django.db import models

# Create your models here.
class Dept(models.Model):
    Dept_no=models.IntegerField(primary_key=True)
    Dname=models.CharField(max_length=100)
    Loc=models.CharField(max_length=100)
    def __int__(self):
        return self.Dept_no
class Emp(models.Model):
    Emp_no=models.IntegerField(primary_key=True)
    Ename=models.CharField(max_length=100)
    Job=models.CharField(max_length=100)
    MGR=models.IntegerField()
    Hire_date=models.DateField()
    Sal=models.IntegerField()
    Dept_no=models.ForeignKey(Dept,on_delete=models.CASCADE)
    def __int__(self):
        return self.Emp_no
