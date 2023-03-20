from django.db import models
from user.models import * 

# Create your models here.

technology_choice = (('django','Django'),('spring','Spring'),('mern','Mern'),('mean','Mean'),('php','PHP'))

class Project(models.Model):

    title = models.CharField(max_length=30)
    description = models.TextField(max_length=500, null=True) 
    technology = models.CharField(choices=technology_choice,max_length=100)
    estimatedHours = models.PositiveIntegerField()
    startDate = models.DateField()
    endDate = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Project'
    
    def __str__(self):
        return self.title

class ProjectTeam(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Project_Team'

status_choice = (('block','Block'), ('pending','Pending'), ('completed','Completed'))

class Status(models.Model):
    
    statusName = models.CharField(choices=status_choice ,max_length=20)
    
    class Meta:
        db_table = 'Status'
    
    def __str__(self):
        return self.statusName

class ProjectModule(models.Model):
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    moduleName = models.CharField(max_length=30)
    description = models.CharField(max_length=100, null=True)
    estimatedHours = models.IntegerField()
    status = models.BooleanField(default=True)
    startDate = models.DateField()
    
    class Meta:
        db_table = 'Project_Module'
    
    def __str__(self):
        return self.moduleName

priority_choice = (('low','Low'),('medium','Medium'),('high','High'))

class Task(models.Model):
    
    module= models.ForeignKey(ProjectModule, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    priority = models.CharField(choices= priority_choice, max_length=30, null=True)
    description = models.TextField(max_length=500)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    totalMinutes = models.IntegerField()

    class Meta:
        db_table = 'Task'
    
    def __str__(self):
        return self.title

class UserTask(models.Model): 
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    class Meta:
        db_table = 'User_Task'