import plotly
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.cache import never_cache
from rest_framework_simplejwt.tokens import RefreshToken

from backend.nlp.plots import valueCounter, stackedPlot, multipleLinesGraph
from .serializers import FileSerializer
from backend.nlp.bapCleanAndTokenize import clean_and_tokenize, clean_and_tokenize_v2
from .models import File
import json

from backend.nlp.prepareData import *

index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class UploadFile(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        request.data['user'] = request.user.id
        request.data['json'] = request.data['file'].open().read()

        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():

            file_serializer.save()

            return Response({'success': True}, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CleanWithParameters(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        document = File.objects.get(uuid=request.data['uuid'])
        parameters = request.data['checkboxes']
        most_common = int(request.data['mostCommon'])

        data = clean_and_tokenize_v2(document.file, parameters, most_common)

        return Response(data, status=status.HTTP_200_OK)


class Query(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
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
            document = File.objects.get(id=request.data['id'], user=request.user)
            document.delete()

            return Response({'success': True})
        except Exception:
            return Response({'success': False})


class Stats(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        document = File.objects.get(uuid=request.data['uuid'])

        data = json.load(document.file)

        d = {}
        for item in data['source']:
            if data['source'][item] in d:
                d[data['source'][item]] = d.get(data['source'][item]) + 1
            else:
                d[data['source'][item]] = 1

        return Response(d, status=status.HTTP_200_OK)


class PlotData(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        """
        :params uuid,type,category,number: in order to create
        graph give this params
        :examples:
        /api/plot/?type=valueCounter&category=source&number=10&uuid=c26f8410-a56c-11e9-865f-1fc3cb66546c
        /api/plot/?type=stackedPlot&category1=date&category2=source&uuid=c26f8410-a56c-11e9-865f-1fc3cb66546c
        /api/plot/?type=multipleLinesGraph&category1=cn&category2=source&uuid=c26f8410-a56c-11e9-865f-1fc3cb66546c

        :return: dash figure data in json format
        """
        document = File.objects.get(uuid=request.GET['uuid'])

        plot_type = request.GET['type']
        dataframe = getFile(document.json)

        if plot_type == "valueCounter":
            category = request.GET['category']
            number = int(request.GET['number'])
            figure = valueCounter(category, number, dataframe)

            data = json.dumps(figure, cls=plotly.utils.PlotlyJSONEncoder)
            return Response(data, status=status.HTTP_200_OK)

        if plot_type == "stackedPlot":
            category1 = request.GET['category1']
            category2 = request.GET['category2']
            figure = stackedPlot(category1, category2, dataframe)

            data = json.dumps(figure, cls=plotly.utils.PlotlyJSONEncoder)
            return Response(data, status=status.HTTP_200_OK)

        if plot_type == "multipleLinesGraph":
            category1 = request.GET['category1']
            category2 = request.GET['category2']
            figure = multipleLinesGraph(category1, category2, dataframe)

            data = json.dumps(figure, cls=plotly.utils.PlotlyJSONEncoder)
            return Response(data, status=status.HTTP_200_OK)
