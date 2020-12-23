from django.http import JsonResponse, HttpResponse
import json
from rest_framework.parsers import FormParser, JSONParser
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from crawl_job.lib.common.common import convert_timestamp_in_json_data, get_tag_job
from crawl_job.lib.crawl_job import get_job_title, get_job_detail
from rest_framework.generics import ListAPIView, RetrieveAPIView
from crawl_job.lib.pagination import GetLimitJobPagination, CustomPagination
from crawl_job.models import models
from django.shortcuts import redirect
from crawl_job.serializers import JobTitleSerialiser, JobDetailSerializer


def job_title(request):
    """
    :param request:
    :return: all job title
    """

    if request.method == 'GET':
        list_job = get_job_title()

        return HttpResponse(json.dumps(list_job))


def job_detail(request, job_id):
    if request.method == 'GET':
        list_detail_job = get_job_detail(job_id)
        return HttpResponse(list_detail_job)


def job_list(request):
    if request.method == 'GET':
        job = models.Job.objects.all()
        serializer = JobTitleSerialiser(job, many=True)
        pagination_class = GetLimitJobPagination
        return JsonResponse(serializer.data, safe=False)


def job_detail_list(request, job_id):
    if request.method == 'GET':
        job = models.Job.objects.filter(job_id=job_id).first()
        serializer = JobDetailSerializer(job, many=False)
        return JsonResponse(serializer.data, safe=False)


class JobDetailList(RetrieveAPIView):
    parser_classes = [JSONParser, FormParser]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'detail.html'
    queryset = job = models.Job.objects.all()
    serializer_class = JobDetailSerializer

    def get(self, request, *args, **kwargs):
        job_id = kwargs['job_id']
        queryset = models.Job.objects.filter(job_id=job_id).first()
        serializer = self.get_serializer(queryset, many=False)
        data = serializer.data
        payload = {
            'return_code': '0000',
            'return_message': 'Success',
            'data': data['content']
        }
        return Response({"json_result": payload})


class GetJobList(ListAPIView):
    pagination_class = CustomPagination
    parser_classes = [JSONParser, FormParser]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'
    queryset = models.Job.objects.all()
    serializer_class = JobTitleSerialiser

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            result = self.get_paginated_response(serializer.data)
            data = result.data  # pagination data
        else:
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data

        data = convert_timestamp_in_json_data(data)
        # data = get_tag_job(data)
        payload = {
            'return_code': '0000',
            'return_message': 'Success',
            'data': data
        }

        return Response({"json_result": payload})

    def post(self, request, *args, **kwargs):
        keyword_search = request.POST.get("job_keywords", "")
        payload = {
            'return_code': '0000',
            'return_message': 'Success',
        }
        if keyword_search:
            queryset = []
            for keyword in keyword_search.split(" "):
                queryset += self.queryset.filter(job_detail__contains=keyword)
            page = self.paginate_queryset(queryset)
            serializer = self.get_serializer(page, many=True)
            result = self.get_paginated_response(serializer.data)
            data = convert_timestamp_in_json_data(result.data)
            # data = get_tag_job(data)
            payload['data'] = data
            return Response({"json_result": payload})
        else:
            payload["return_message"] = "can not found any job"
            return Response({"json_result": payload})


def error404(request, *args, **kwargs):
    return redirect('/')
