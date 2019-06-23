
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *

urlpatterns = [
    # Signup endpoints
    path('user/signup/', CreateUserView.as_view(), name='register'),

    # Sign in and JWT Auth endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Needs Title
    path('files/', GetFilesOfUser.as_view(), name='get_files'),

    # NLP Process endpoints
    path('upload/', UploadFile.as_view(), name='file_upload'),
    path('cleaning/', CleanWithParameters.as_view(), name='cleaning'),
    path('query/', Query.as_view(), name='query'),

    # Test
    path('stats/', Stats.as_view())
]
