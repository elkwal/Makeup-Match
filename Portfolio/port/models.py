from django.db import models

# Create your models here.
class Project(models.Model):
    project_title = models.CharField(max_length=50)
    project_image = models.ImageField(upload_to='projects/')
    project_description = models.TextField()
    project_site = models.CharField(max_length=100)

    def __str__(self):
        return self.project_title

class Skill(models.Model):
    skill_title = models.CharField(max_length=50)
    skill_icon = models.ImageField(upload_to='skills/')

    def __str__(self):
        return self.skill_title
