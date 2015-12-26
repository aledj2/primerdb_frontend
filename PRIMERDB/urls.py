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
from django.conf.urls import include, url, patterns
from django.contrib import admin
from frontend.forms import *
from frontend.views import add_primer_design_wizard
from django.conf import settings

#x=''
#if settings.DEBUG:
    #import debug_toolbar
    #x=url(r'^__debug__/', include(debug_toolbar.urls)),

urlpatterns = [
    url(r'^$','frontend.views.login', name='home'),
    url(r'^add_primer_design/$','frontend.views.add_primer_design',name='add_primer_design'),
    url(r'^add_primer_design_wizard/$', add_primer_design_wizard.as_view([add_new_primer1, add_new_primer2, add_new_primer3, add_new_primer4])),#, add_new_primer_summary])),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/$','frontend.views.auth_view', name='auth_view'),
    url(r'^bad_user/$','frontend.views.bad_user', name='bad_user'),
    # find amplicon design
    url(r'^find_amplicon_design/$','frontend.views.find_amplicon_design', name='find_amplicon_design'),
    url(r'^findampliconbycoord/$','frontend.views.findampliconbycoord', name='findampliconbycoord'),
    url(r'^findampliconbygene/$','frontend.views.find_amplicon_by_gene_select_gene', name='find_amplicon_by_gene_select_gene'),
    url(r'^findampliconbygene/(?P<geneshgncid>[0-9]+)/$','frontend.views.find_amplicon_by_gene_select_exons', name='find_amplicon_by_gene_select_exons'),
    url(r'^findampliconbygene/(?P<geneshgncid>[0-9]+)/(?P<exon>[0-9]+)/$','frontend.views.display_amplicon_matching_geneexon', name='display_amplicon_matching_geneexon'),
    url(r'^findampliconbyprimername/$','frontend.views.findampliconbyprimername', name='findampliconbyprimername'), 
    url(r'^amplicon_design/(?P<productkey>[0-9]+)/$','frontend.views.amplicon_design', name='amplicon_design'),
    #find primer design
    url(r'^findprimerbycoord/$','frontend.views.findprimerbycoord', name='findprimerbycoord'),
    url(r'^findprimerbygene/$','frontend.views.find_primer_by_gene_select_gene', name='find_primer_by_gene_select_gene'),
    url(r'^findprimerbygene/(?P<geneshgncid>[0-9]+)/$','frontend.views.find_primer_by_gene_select_exons', name='find_primer_by_gene_select_exons'),
    url(r'^findprimerbygene/(?P<geneshgncid>[0-9]+)/(?P<exon>[0-9]+)/$','frontend.views.display_primers_matching_geneexon', name='display_primers_matching_geneexon'),
    url(r'^findprimerbyprimername/$','frontend.views.findprimerbyprimername', name='findprimerbyprimername'),
    url(r'^primer_design/(?P<primerkey>[0-9]+)/$','frontend.views.primer_design', name='primer_design'),
    
    url(r'^find_primer_design/$','frontend.views.find_primer_design',name='find_primer_design'),
    url(r'^home/$', 'frontend.views.login', name='home'),
    url(r'^login/$','frontend.views.login', name='login'),    
    url(r'^sorry_login_required/$','frontend.views.sorry_login_required', name='sorry_login_required'),    
    url(r'^logout/$','frontend.views.logout', name='logout'),
    url(r'^name/$','frontend.views.name', name = 'name'),
    #url(r'^new_primer_design_summary/$',frontend.views)
    url(r'^primer_info/$','frontend.views.primer_info', name='primer_info'),
    url(r'^testoutput/$','frontend.views.test_output', name='test_output'),
    url(r'^register/$','frontend.views.register_user', name='register_user'),
    url(r'^register_success/$','frontend.views.register_success', name='register_success'),
    # url(r'^view1/$','frontend.views.view1',name='view1'),
    url(r'^welcome/$','frontend.views.welcome', name='welcome'),
    #x
    ]


