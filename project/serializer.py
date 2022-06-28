from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from .models import Project, Issue, Comment, Contributor


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type']


class ProjectDetailSerializer(ModelSerializer):
    issues = StringRelatedField(many=True)
    users = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'issues', 'users']


class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ['id', 'author', 'title', 'description', 'tag', 'priority', 'project', 'status',
                  'assignee', 'created_time']


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['user', 'role', 'project']
