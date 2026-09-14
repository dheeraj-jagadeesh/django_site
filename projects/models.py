from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    github_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title