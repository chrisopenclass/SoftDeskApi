from .views import ProjectViewSet, IssueViewSet, CommentViewSet, ContributorsViewset
from rest_framework_nested import routers
from django.urls import path, include


router = routers.SimpleRouter()
router.register(r'projects', ProjectViewSet)

projects_router = routers.NestedSimpleRouter(router, "projects", lookup="project")
projects_router.register(r'issues', IssueViewSet, basename="projects-issues")
projects_router.register(r'users', ContributorsViewset, basename="projects-contributor")

issues_router = routers.NestedSimpleRouter(projects_router, r'issues', lookup="issue")
issues_router.register(r'comments', CommentViewSet, basename="issues-comments")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(projects_router.urls)),
    path("", include(issues_router.urls)),
]
