from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from .models import Project, Issue, Comment, Contributor


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author']


class ProjectDetailSerializer(ModelSerializer):
    issues = StringRelatedField(many=True)
    users = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author', 'issues', 'users']


class IssueSerializer(ModelSerializer):
    assignee_user_id = StringRelatedField()

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'tag', 'priority', 'project_id', 'status', 'author',
                  'assignee_user_id', 'created_time', 'comments']


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class ContributorSerializer(ModelSerializer):
    user_id = StringRelatedField()

    class Meta:
        model = Contributor
        fields = ['user_id', 'role']
