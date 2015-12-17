"""PRIMERDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'frontend.views.home', name='home'),
    url(r'^home/', 'frontend.views.home', name='home'),
    url(r'^view1','frontend.views.view1',name='view1'),
    url(r'^chromosome/','frontend.views.chromosome_page', name = 'chromosome_page'),
    url(r'^chromosome/', 'frontend.views.chromosome_home', name = 'chromosome_home'),
    url(r'^name/','frontend.views.name', name = 'name'),
    url(r'^primer_info','frontend.views.primer_info', name='primer_info'),
]
