from django.db import models
from django.conf import settings


TYPE_CHOICES = [
    ('BACKEND', 'BACKEND'),
    ('FRONTEND', 'FRONTEND'),
    ('IOS', 'IOS'),
    ('ANDROID', 'ANDROID')
]
PRIORITY_CHOICES = [
    ('LOW', 'LOW'),
    ('MEDIUM', 'MEDIUM'),
    ('HIGH', 'HIGH'),
]
STATS_CHOICES = [
    ('TODO', 'TODO'),
    ('IN PROGRESS', 'IN PROGRESS'),
    ('DONE', 'DONE'),
]
TAG_CHOICES = [
    ('BUG', 'BUG'),
    ('UPGRADE', 'UPGRADE'),
    ('TASK', 'TASK'),
]
ROLE = [
    ('AUTHOR', 'AUTHOR'),
    ('CONTRIBUTOR', 'CONTRIBUTOR'),
]


class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    type = models.CharField(choices=TYPE_CHOICES, max_length=128)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='author', on_delete=models.CASCADE)


class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='contributors')
    role = models.CharField(choices=ROLE, default='CONTRIBUTOR', max_length=128)


class Issue(models.Model):
    title = models.CharField(max_length=128)
    desc = models.TextField(max_length=2048)
    tag = models.CharField(choices=TAG_CHOICES, max_length=100)
    priority = models.CharField(choices=PRIORITY_CHOICES, default='LOW', max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(choices=STATS_CHOICES, default='TODO', max_length=100)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    assignee = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = models.CharField(max_length=2048)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
