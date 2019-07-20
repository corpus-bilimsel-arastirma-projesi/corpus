from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *

file_patterns = [
    path('', GetFilesOfUser.as_view()),
    path('stats/', Stats.as_view()),
    path('upload/', UploadFile.as_view()),
    path('concat/', ConcatFile.as_view()),
    path('add-date-column/', AddDateColumn.as_view()),
    path('delete-between/', DeleteBetween.as_view()),
    path('delete-word/', DeleteWord.as_view()),
    path('delete-contain/', DeleteContain.as_view()),
    path('delete-beginning/', DeleteBeginning.as_view()),
    path('delete-end/', DeleteEnd.as_view()),
    path('replace-words/', ReplaceWords.as_view()),
]

urlpatterns = [

    path('file/', include(file_patterns)),

    # Signup endpoints
    path('user/signup/', CreateUserView.as_view(), name='register'),

    # Sign in and JWT Auth endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # NLP Process endpoints
    path('query/', Query.as_view()),

    path('plot/', PlotData.as_view()),

]
