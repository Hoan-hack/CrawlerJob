# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Job(models.Model):
    id = models.AutoField(primary_key=True)
    job_id = models.IntegerField(blank=True, null=True)
    job_detail = models.TextField(blank=True, null=True)  # This field type is a guess.
    content = models.TextField(blank=True, null=True)
    tag = models.TextField(blank=True, null=True)  # This field type is a guess.
    update_time = models.TextField(blank=True, null=True)  # This field type is a guess.
    create_time = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'job'
