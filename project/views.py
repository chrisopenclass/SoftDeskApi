from .models import Issue, Project, Contributor, Comment
from rest_framework import viewsets, status
from .serializer import (
    ProjectSerializer,
    ContributorSerializer,
    CommentSerializer,
    IssueSerializer,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .permissions import IsAuthorOrReadOnly


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(
            contributors__user=self.request.user.id)

    def create(self, request):
        data = request.data.copy()
        author = request.user.id
        data = request.data.copy()
        serialized_data = ProjectSerializer(data=data)
        serialized_data = ProjectSerializer(data={
            **dict(data.items()),
            "author": author,
        })
        serialized_data.is_valid(raise_exception=True)
        project = serialized_data.save()
        contributor = Contributor.objects.create(
            user=request.user,
            project=project,
        )
        contributor.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        data = request.data.copy()
        instance = self.get_object()
        serializer = ProjectSerializer(data={
            **dict(data.items()),
            "id": instance.id,
            "author": instance.author.id,
        })
        serializer.is_valid(raise_exception=True)
        return super().update(serializer, status=status.HTTP_201_CREATED)


class ContributorsViewset(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Contributor.objects.filter(project=self.kwargs["project_pk"])

    def create(self, request, project_pk):
        project = project_pk
        data = request.data.copy()
        serialized_data = ContributorSerializer(data=data)
        serialized_data = ContributorSerializer(data={
            **dict(data.items()),
            "project": project,
        })
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)


class IssueViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs["project_pk"])

    def create(self, request, project_pk=None):
        data = request.data.copy()
        author = request.user.id
        serialized_data = IssueSerializer(data={
            **dict(data.items()),
            "author": author,
            "project": project_pk,
        })
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)


class CommentViewSet(viewsets.ModelViewSet, IsAuthorOrReadOnly):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def create(self, request, issue_pk=None, project_pk=None):
        data = request.data.copy()
        author = request.user.id
        serialized_data = CommentSerializer(data={
            **dict(data.items()),
            "author": author,
            "issue": issue_pk,
        })
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return Comment.objects.filter(issue=self.kwargs["issue_pk"])

    def update(self, request, project_pk=None, issue_pk=None, comment_pk=None, pk=None):
        data = request.data.copy()
        instance = self.get_object()
        serializer = CommentSerializer(data={
            **dict(data.items()),
            "id": instance.id,
            "author": instance.author.id,
            "issue": instance.issue.id,
        })
        serializer.is_valid(raise_exception=True)
        return super().update(serializer, status=status.HTTP_201_CREATED)
