# models.py

from django.db import models

class UserStory(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_team_member = models.CharField(max_length=50)
    fetched_from_Jira = models.BooleanField(default=False)

    def __str__(self):
        return self.title