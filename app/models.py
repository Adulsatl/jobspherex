from django.db import models
from django.contrib.auth.models import User

class table(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=20,null=True)
    lastname=models.CharField(max_length=20,null=True)
    email=models.EmailField(max_length=30,null=True)
    number=models.IntegerField(null=True)
    username=models.CharField(max_length=10,null=True)
    password=models.CharField(max_length=8,null=True)
    image=models.ImageField(null=True)

class company_reg(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    c_name=models.CharField(max_length=20,null=True)
    c_email=models.EmailField(max_length=30,null=True)
    c_number=models.IntegerField(null=True)
    c_location=models.CharField(max_length=110,null=True)
    c_licence=models.IntegerField(null=True)
    c_industry=models.CharField(max_length=125,null=True)
    c_year=models.IntegerField(null=True)
    c_password=models.CharField(max_length=8,null=True)
    
class reg(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    u_firstname=models.CharField(max_length=20,null=True)
    u_lastname=models.CharField(max_length=20,null=True)
    u_email=models.EmailField(max_length=30,null=True)
    u_number=models.IntegerField(null=True)
    u_username=models.CharField(max_length=10,null=True)
    u_password=models.CharField(max_length=8,null=True)
    u_image=models.ImageField(null=True)

class job(models.Model):
    user=models.ForeignKey(company_reg,on_delete=models.CASCADE)
    job_details=models.CharField(max_length=50,null=True)
    job_description=models.TextField(max_length=500,null=True)
    company_name=models.CharField(max_length=50,null=True)
    skills=models.CharField(max_length=100,null=True)
    experience=models.CharField(max_length=40,null=True)
    qualification=models.CharField(max_length=100,null=True)
    benifits=models.CharField(max_length=100,null=True)
    pay_types=models.CharField(max_length=100,null=True)
    salary=models.IntegerField(null=True)
    date=models.DateField(null=True)
    
class applicant_form(models.Model):
    user=models.ForeignKey(reg,on_delete=models.CASCADE)
    job=models.ForeignKey(job,on_delete=models.CASCADE)
    fullname=models.CharField(max_length=25,null=True)
    email=models.EmailField(max_length=100,null=True)
    num=models.IntegerField(null=True)
    relocate=models.CharField(max_length=20,null=True)
    u_location=models.CharField(max_length=20,null=True)
    resume=models.FileField(null=True)
    

