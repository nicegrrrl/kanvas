from django.urls import path
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path(
        "courses/<str:course_id>/students/",
        jwt_views.RetrieveUpdateStudentView.as_view(),
    ),
]
