from rest_framework import serializers

from crawl_job.models import models


class JobTitleSerialiser(serializers.ModelSerializer):
    class Meta:
        model = models.Job
        fields = ["job_id", "job_detail", "tag", "create_time"]


class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Job
        fields = ["job_id", "job_detail", "tag", "content", "create_time"]
