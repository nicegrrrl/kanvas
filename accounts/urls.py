from django.urls import path
from .views import CreateAccountView
from rest_framework_simplejwt import views as jwt_views
# from rest_framework_simplejwt.views import token_obtain_pair


urlpatterns = [
  path("accounts/", CreateAccountView.as_view()),
  path("login/", jwt_views.TokenObtainPairView.as_view())
  # path("login/", token_obtain_pair)
]
