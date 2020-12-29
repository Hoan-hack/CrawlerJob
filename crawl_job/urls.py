"""crawl_job URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404

import crawl_job
from crawl_job.views import job_title, job_detail, GetJobList, JobDetailList

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('job_title/', job_title),
    path('job_detail/<int:job_id>/', job_detail),
    # path('job_list/', job_list),
    path('', GetJobList.as_view()),
    # path('job_detail_list/<int:job_id>/', job_detail_list),
    path('job_detail_list/<int:job_id>/', JobDetailList.as_view()),
]

handler404 = crawl_job.views.error404
