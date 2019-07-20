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

from backend.nlp.plots import value_counter, stacked_plot, multiple_lines_graph
from .serializers import FileSerializer
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
        request.data['edited_json'] = request.data['file'].open().read()

        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():

            file_serializer.save()

            return Response({'success': True}, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        document = File.objects.get(id=request.data['id'])

        data = json.load(document.json)

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
        :params id,type,category,number: in order to create
        graph give this params
        :examples:
        /api/plot/?type=value_counter&category=source&number=10&id=c26f8410-a56c-11e9-865f-1fc3cb66546c
        /api/plot/?type=stackedPlot&category1=date&category2=source&id=c26f8410-a56c-11e9-865f-1fc3cb66546c
        /api/plot/?type=multipleLinesGraph&category1=cn&category2=source&id=c26f8410-a56c-11e9-865f-1fc3cb66546c

        :return: dash figure data in json format
        """
        document = File.objects.get(id=request.GET['id'])

        plot_type = request.GET['type']
        data_frame = json_to_data_frame(document.edited_json)

        if plot_type == "value-counter":
            category = request.GET['category']
            number = int(request.GET['number'])
            figure = value_counter(category, number, data_frame)

            data = json.dumps(figure, cls=plotly.utils.PlotlyJSONEncoder)
            return Response(data, status=status.HTTP_200_OK)

        if plot_type == "stacked-plot":
            category1 = request.GET['category1']
            category2 = request.GET['category2']
            figure = stacked_plot(category1, category2, data_frame)

            data = json.dumps(figure, cls=plotly.utils.PlotlyJSONEncoder)
            return Response(data, status=status.HTTP_200_OK)

        if plot_type == "multiple-lines-graph":
            category1 = request.GET['category1']
            category2 = request.GET['category2']
            figure = multiple_lines_graph(category1, category2, data_frame)

            data = json.dumps(figure, cls=plotly.utils.PlotlyJSONEncoder)
            return Response(data, status=status.HTTP_200_OK)


class ConcatFile(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        files = request.data['files']
        file_name = request.data['file_name']

        files_to_concat = []

        for file in files:
            file = File.objects.get(id=file)
            file_json_data_frame = json_to_data_frame(file.json)
            files_to_concat.append(file_json_data_frame)

        data_frames = file_concat(files_to_concat)

        protected_file = files.pop()
        protected_file = File.objects.get(id=protected_file)

        protected_file.edited_json = data_frames
        protected_file.file_name = file_name
        protected_file.save()

        for file in files:
            file = File.objects.get(id=file)
            file.delete()

        return Response({'success': True})


class AddDateColumn(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        date_var = request.data['date_var']
        file = File.objects.get(id=request.data['id'])
        data_frame = json_to_data_frame(file.edited_json)

        file.edited_json = choose_date(date_var, data_frame)
        file.save()

        return Response({'success': True})


class DeleteBetween(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        start_word = request.data['start_word']
        end_word = request.data['end_word']

        file = File.objects.get(id=request.data['id'])
        data_frame = json_to_data_frame(file.edited_json)

        file.edited_json = delete_between(start_word, end_word, data_frame)
        file.save()

        return Response({'success': True})


class DeleteWord(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        word = request.data['word']
        file = File.objects.get(id=request.data['id'])
        data_frame = json_to_data_frame(file.edited_json)

        file.edited_json = delete_word(word, data_frame)
        file.save()

        return Response({'success': True})


class DeleteContain(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        word = request.data['word']
        file = File.objects.get(id=request.data['id'])
        data_frame = json_to_data_frame(file.edited_json)

        file.edited_json = delete_contain(word, data_frame)
        file.save()

        return Response({'success': True})


class DeleteBeginning(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        start = request.data['start']
        file = File.objects.get(id=request.data['id'])
        data_frame = json_to_data_frame(file.edited_json)

        file.edited_json = delete_beginning(start, data_frame)
        file.save()

        return Response({'success': True})


class DeleteEnd(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        end = request.data['end']
        file = File.objects.get(id=request.data['id'])
        data_frame = json_to_data_frame(file.edited_json)

        file.edited_json = delete_end(end, data_frame)
        file.save()

        return Response({'success': True})


class ReplaceWords(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        word_list = request.data['word_list']
        target_word = request.data['target_word']
        file = File.objects.get(id=request.data['id'])
        data_frame = json_to_data_frame(file.edited_json)

        file.edited_json = replace_words(word_list, target_word, data_frame)
        file.save()

        return Response({'success': True})


class ColumnMapping(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        file = File.objects.get(id=request.data['id'])
        columns = request.data['columns']
        data_frame = json_to_data_frame(file.json)

        file.edited_json = column_mapping(columns, data_frame)
        file.is_ready = True
        file.save()

        return Response({'success': True})


class ColumnNames(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, id):
        file = File.objects.get(id=id)
        data_frame = json_to_data_frame(file.json)
        columns = column_names(data_frame)

        return Response({'success': True, 'columns': columns})
