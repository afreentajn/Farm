from django.db import models
from django.utils import timezone

# Farm model
class Farm(models.Model):
    name = models.CharField(max_length=100, default='Unnamed Farm')
    location = models.CharField(max_length=255)
    established_on = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

# Field model (a farm can have multiple fields)
class Field(models.Model):
    farm = models.ForeignKey(Farm, related_name='fields', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    area = models.FloatField(help_text="Area in square meters")
    soil_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.farm.name}"

# Crop model (associated with a field)
class Crop(models.Model):
    field = models.ForeignKey(Field, related_name='crops', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    planted_date = models.DateField(default=timezone.now)
    harvest_date = models.DateField()

    def __str__(self):
        return f"{self.name} at {self.field.name}"

# Project model
class Project(models.Model):
    name = models.CharField(max_length=200, default='Unnamed Project')
    farm = models.ForeignKey(Farm, related_name='projects', on_delete=models.CASCADE)
    start_date = models.DateField(default=timezone.now)
    deadline = models.DateField()
    status = models.CharField(max_length=50, default='Ongoing')

    def __str__(self):
        return self.name

# Task model (related to project)
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField()
    assigned_to = models.CharField(max_length=100)
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Pending')

    def __str__(self):
        return self.title
