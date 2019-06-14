from django.contrib.auth.models import User
from django.views.generic import TemplateView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.cache import never_cache
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import FileSerializer
from backend.nlp.bapCleanAndTokenize import clean_and_tokenize, clean_and_tokenize_v2
from .models import File
import json

index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class UploadFile(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        request.data['user'] = request.user.id

        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():

            file_serializer.save()
            data = clean_and_tokenize(request.data['file'])

            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CleanWithParameters(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        document = File.objects.get(uuid=request.data['uuid'])
        parameters = request.data['checkboxes']
        most_common = int(request.data['mostCommon'])

        data = clean_and_tokenize_v2(document.file, parameters, most_common)

        return Response(data, status=status.HTTP_200_OK)


class Query(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        print(request.user.username)

        query = request.data['query']
        query_set = File.objects.filter(file__contains=query)
        dictionaries = [obj.as_dict() for obj in query_set]
        data = json.dumps({"data": dictionaries})
        return Response(data, status=status.HTTP_200_OK)


class CreateUserView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        try:
            user = User.objects.create_user(username, password)

            refresh = RefreshToken.for_user(user)

            token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response({'success': True, 'token': token})
        except Exception:
            return Response({'success': False})


class GetFilesOfUser(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        query_set = File.objects.filter(user=request.user)
        dictionaries = [obj.as_dict() for obj in query_set]
        data = json.dumps({"data": dictionaries})
        return Response(data, status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        try:
            document = File.objects.get(id=request.data['id'])
            document.delete()

            return Response({'success': True})
        except Exception:
            return Response({'success': False})
