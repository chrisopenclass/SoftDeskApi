from rest_framework.relations import StringRelatedField
from rest_framework import serializers

from .models import Project, Issue, Comment, Contributor


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author']


class ProjectDetailSerializer(serializers.ModelSerializer):
    issues = StringRelatedField(many=True)
    users = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'issues', 'users']


class ContributorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['user', 'role', 'project']


class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'tag', 'priority', 'status',
                  'assignee']
        read_only_fields = ['author', 'project', 'created_time']

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id',
                  'description',
                  'created_time',
                  'author',
                  'issue'
                  ]
