from django.conf.urls import url
from .views import *

urlpatterns = [
    url('upload/', UploadFile.as_view(), name='file-upload'),
    url('cleaning/', CleanWithParameters.as_view(), name='cleaning'),
    url('query/', Query.as_view(), name='query'),
    url('test/', Test.as_view())
]
