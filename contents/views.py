from rest_framework.generics import (
    CreateAPIView,
    get_object_or_404,
    RetrieveUpdateDestroyAPIView,
)
from contents.models import Content
from contents.serializers import ContentSerializer
from courses.models import Course
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsSuperUser, ContentPermission
from rest_framework.views import Response, status
from rest_framework.exceptions import NotFound


class CreateContentView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsSuperUser]

    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def perform_create(self, serializer):
        pk = self.kwargs["course_id"]
        course = Course.objects.get(pk=pk)
        if not course:
            return Response({"detail": "course not found."}, status.HTTP_404_NOT_FOUND)
        course = get_object_or_404(Course, pk=pk)
        serializer.save(course=course)


class RetrieveUpdateDestroyContentView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [ContentPermission]

    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "content_id"

    def get_object(self):
        try:
            Course.objects.get(pk=self.kwargs["course_id"])
            content = Content.objects.get(pk=self.kwargs["content_id"])
        except Course.DoesNotExist:
            raise NotFound({"detail": "course not found."})
        except Content.DoesNotExist:
            raise NotFound({"detail": "content not found."})
        self.check_object_permissions(self.request, content)
        return content
