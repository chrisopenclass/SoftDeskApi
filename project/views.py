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
        serialized_data = ProjectSerializer(data=data)
        serialized_data.is_valid(raise_exception=True)
        project = serialized_data.save()

        contributor = Contributor.objects.create(
            user=request.user,
            project=project,
        )
        contributor.save()

        return Response(serialized_data.data, status=status.HTTP_201_CREATED)


class ContributorsViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    serializer_class = ContributorSerializer

    def get_queryset(self):
        return Contributor.objects.filter(project_id=self.kwargs["project_pk"])

    def create(self, request, project_pk=None):
        data = request.data.copy()
        user = data["user"]
        if Contributor.objects.filter(project_id=project_pk, user_id=user):
            return Response("User already added.", status=status.HTTP_400_BAD_REQUEST)
        serialized_data = ContributorSerializer(data={
            "project": project_pk,
            "user": user,
            "role": data["role"]
        })
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, project_pk, pk):
        Contributor.objects.filter(project_id=project_pk, user_id=pk).delete()
        return Response("Deleted", status=status.HTTP_200_OK)


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
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
