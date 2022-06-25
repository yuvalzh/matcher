from django.db import models

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=50,primary_key=True)

class Candidate(models.Model):
    title = models.CharField(max_length=50) #job_name
    skills = models.ManyToManyField(Skill)

class Job(models.Model):
    title = models.CharField(max_length=50,primary_key=True)
    skills = models.ManyToManyField(Skill)
    
    