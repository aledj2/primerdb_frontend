
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response
from django.shortcuts import render, get_object_or_404
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.db.models import Q
from .models import Chromosome, Primerinformation, Pcrproducts, Primerinfo, Blat, Item, Geneshgnc140714, Snpcheck, Storage, Audit
from .forms import *
import operator
from formtools.wizard.views import SessionWizardView


addprimerdesignforms=[("page1", add_new_primer1),("page2", add_new_primer2),("page3", add_new_primer3),("page4", add_new_primer4)]#,("page5", add_new_primer_summary)]
addprimerdesigntemplates = {"0":"frontend/addprimerdesignwizard.html", "1":"frontend/addprimerdesignwizard.html","2":"frontend/addprimerdesignwizard.html", "3":"frontend/addprimerdesignwizard.html"}#}, "4":"frontend/new_primer_design_summary.html"}

#@login_required(login_url='/sorry_login_required/')
class add_primer_design_wizard(SessionWizardView):

    def get_context_data(self, form, **kwargs):
        args = super(add_primer_design_wizard, self).get_context_data(form=form, **kwargs)
        if self.steps.current == '4':
            args.update({'all_data': self.get_all_cleaned_data()})
        return args

    def get_template_names(self):
        return [addprimerdesigntemplates[self.steps.current]]

    def done(self,form_list,form_dict,**kwargs):
        args={}
        for i in form_dict:
            data = super(add_primer_design_wizard, self).get_context_data(form=i, **kwargs)
            args.update({'all_data': self.get_all_cleaned_data()})
        
        gene=args['all_data']['gene']
        exon=args['all_data']['exon']
        exon2=args['all_data']['exon']
        chrom=args['all_data']['chromosome']
        #primername=
        sequence=args['all_data']['sequence']
        mod=args['all_data']['tag']
        pcrcond=args['all_data']['pcrconditions']
        pcrprogram=args['all_data']['pcrprogram']
        assay=args['all_data']['assay']
        ucsc=args['all_data']['ucsc']
        
        if Primerinformation.objects.filter(geneshgncid=gene).filter(exon=exon).exists():
            max_current_version=Primerinformation.objects.filter(geneshgncid=gene).filter(exon=exon).values_list('version',flat=True).order_by('-version')[:1]
            list=[]
            list.extend(max_current_version)
            for i in list:
                new_version=int(i)+1
        else:
            new_version=333

        
        item_version=Item.objects.filter(itemid=new_version).get()
        version_text=item_version.item
        
        item_tag=Item.objects.filter(itemid=mod).get()
        tag_text=item_tag.item
        
        gene_entry=Geneshgnc140714.objects.filter(geneshgncid=gene).get()
        gene_entry.used=1
        gene_entry.save()
        genename=gene_entry.approvedsymbol



        primername=genename+"_ex"+str(exon)+"_"+tag_text+"_"+version_text

        commit=True
        primer=Primerinformation(geneshgncid=gene, exon=exon, exon_2=exon2, sequence=sequence, chromosome=chrom, modification=mod, pcrconditions=pcrcond, pcrprogram=pcrprogram, ucsc=ucsc, assay=assay, version=new_version, primername=primername)

        if commit:
            primer.save()
            primerkey=primer.primerkey
        
        strand=args['all_data']['strand']
        start=args['all_data']['start']
        stop=args['all_data']['stop']
        genomebuild=args['all_data']['genomebuild']
        
        blat=Blat(primerkey=primerkey, strand=strand, start=start, stop=stop, genomebuild=genomebuild)
        blat.save()

        result=args['all_data']['result']
        snpchecked=args['all_data']['snpchecked']
        datechecked=args['all_data']['dateofsnpcheck']
        dbbuild=args['all_data']['dbbuild']
        rs1=args['all_data']['rs1']
        rs2=args['all_data']['rs2']
        rs3=args['all_data']['rs3']
        nt=args['all_data']['nt']
        notes=args['all_data']['notes']
        validated=args['all_data']['validated']

        snpcheck=Snpcheck(result=result,snpchecked=snpchecked,dateofsnpcheck=datechecked,dbbuild=dbbuild,rs1=rs1,rs2=rs2,rs3=rs1,nt=nt,notes=notes,validated=validated, primerkey=primerkey)
        snpcheck.save()
        
        #pk=primerkey
        return HttpResponseRedirect("/primer_design/"+str(primerkey))
        #return primer_design(primerkey)


@login_required(login_url='/sorry_login_required/')
def amplicon_design(request, productkey):
    args={}
    productid = int(productkey)
    args['productid']=productid
    pcrproducts_table=Pcrproducts.objects.all()
    args['pcrproducts']=pcrproducts_table
    primerinformation = Primerinformation.objects.all()
    args['primerinformation']=primerinformation
    storage = Storage.objects.all()
    args['storage'] = storage
    return render_to_response("frontend/amplicon_design.html", args,context_instance=RequestContext(request))


def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/welcome/')
    else:
        return HttpResponseRedirect('/bad_user/')

def bad_user(request):
    return render_to_response('frontend/bad_user.html',context_instance=RequestContext(request))

# find amplicons
@login_required(login_url='/sorry_login_required/')
def find_amplicon_design(request):
    args={}
    args.update(csrf(request))
    return render_to_response('frontend/findamplicondesign.html',args, context_instance=RequestContext(request))

@login_required(login_url='/sorry_login_required/')
def find_amplicon_by_gene_select_exons(request, geneshgncid):
    args={}
    geneid=int(geneshgncid)
    args['geneshgncid']=int(geneshgncid)

    if request.POST:
        submittedform = findampliconbygene_selectexon(request.POST)
        #submittedform.save()
        exon=request.POST.get("exon","")
        return HttpResponseRedirect("/findampliconbygene/"+str(geneid)+"/"+str(exon))
    else:
        form = findampliconbygene_selectexon(geneid)

    if Primerinformation.objects.filter(geneshgncid=geneid).exists():
        gene=Geneshgnc140714.objects.filter(geneshgncid=geneid).values_list('approvedsymbol',flat=True)
        list=[]
        list.extend(gene)
        for i in list:
            genename=i

    args['gene']=genename
    args.update(csrf(request))
    args['form'] = form
    #return HttpResponse(geneid)
    return render_to_response('frontend/findprimerbygene_exon.html',args, context_instance=RequestContext(request))

@login_required(login_url='/sorry_login_required/')
def display_amplicon_matching_geneexon(request,geneshgncid,exon):
    geneid_input=geneshgncid
    exon_input=exon
    
    args={}
    amplicons=Pcrproducts.objects.all()
    args['amplicons']=amplicons
    primerinformation = Primerinformation.objects.filter(exon=exon_input).filter(geneshgncid=geneid_input).all()
    args['primerinformation']=primerinformation
    args.update(csrf(request))
    return render_to_response('frontend/geneexonampliconresults.html',args, context_instance=RequestContext(request))




@login_required(login_url='/sorry_login_required/')
def find_amplicon_by_gene_select_gene(request):
    if request.POST:
        submittedform = findprimerbygene_selectgene(request.POST)
        if submittedform.is_valid():
            gene=submittedform.cleaned_data['gene']
            return HttpResponseRedirect("/findampliconbygene/"+str(gene))
    else:
        form = findprimerbygene_selectgene
    
    args={}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('frontend/findampliconbygene.html',args, context_instance=RequestContext(request))


@login_required(login_url='/sorry_login_required/')
def display_primers_matching_geneexon(request,geneshgncid,exon):
    geneid_input=geneshgncid
    exon_input=exon
    
    args={}
    primerinformation = Primerinformation.objects.filter(exon=exon_input).filter(geneshgncid=geneid_input).all()
    args['primerinformation']=primerinformation
    args.update(csrf(request))
    return render_to_response('frontend/geneexonprimerresults.html',args, context_instance=RequestContext(request))





#find primers
@login_required(login_url='/sorry_login_required/')
def find_primer_by_gene_select_exons(request, geneshgncid):
    args={}
    geneid=int(geneshgncid)
    args['geneshgncid']=int(geneshgncid)

    if request.POST:
        submittedform = findprimerbygene_selectexon(request.POST)
        #submittedform.save()
        exon=request.POST.get("exon","")
        return HttpResponseRedirect("/findprimerbygene/"+str(geneid)+"/"+str(exon))
    else:
        form = findprimerbygene_selectexon(geneid)

    if Primerinformation.objects.filter(geneshgncid=geneid).exists():
        gene=Geneshgnc140714.objects.filter(geneshgncid=geneid).values_list('approvedsymbol',flat=True)
        list=[]
        list.extend(gene)
        for i in list:
            genename=i

    args['gene']=genename
    args.update(csrf(request))
    args['form'] = form
    #return HttpResponse(geneid)
    return render_to_response('frontend/findprimerbygene_exon.html',args, context_instance=RequestContext(request))


@login_required(login_url='/sorry_login_required/')
def find_primer_by_gene_select_gene(request):
    if request.POST:
        submittedform = findprimerbygene_selectgene(request.POST)
        if submittedform.is_valid():
            gene=submittedform.cleaned_data['gene']
            return HttpResponseRedirect("/findprimerbygene/"+str(gene))
    else:
        form = findprimerbygene_selectgene
    
    args={}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('frontend/findprimerbygene.html',args, context_instance=RequestContext(request))


@login_required(login_url='/sorry_login_required/')
def display_primers_matching_geneexon(request,geneshgncid,exon):
    geneid_input=geneshgncid
    exon_input=exon
    
    args={}
    primerinformation = Primerinformation.objects.filter(exon=exon_input).filter(geneshgncid=geneid_input).all()
    args['primerinformation']=primerinformation
    args.update(csrf(request))
    return render_to_response('frontend/geneexonprimerresults.html',args, context_instance=RequestContext(request))

@login_required(login_url='/sorry_login_required/')
def findprimerbycoord(request):
    if request.POST:
        form = findprimerbycoordform(request.POST)
        if form.is_valid():
            chr = form.cleaned_data['chromosome']
            pos = int(form.cleaned_data['position'])
            start = pos - 500
            stop = pos + 500
            blat_results = Blat.objects.filter(start__gte=start).filter(stop__lte=stop).all()
            list_of_primers_in_range=[]
            for i in blat_results:
                list_of_primers_in_range.append(i.primerkey)
            args2={}
            allprimers = Primerinformation.objects.filter(chromosome=chr).all()
            args2['allprimers']=allprimers
            matchingprimers=list_of_primers_in_range
            args2['matchingprimers']=matchingprimers
            args2.update(csrf(request))
            return render_to_response('frontend/primerresultscoords.html',args2, context_instance=RequestContext(request))

    else:
        form = findprimerbycoordform
    
    args={}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('frontend/findprimerdesignbycoord.html',args, context_instance=RequestContext(request))

@login_required(login_url='/sorry_login_required/')
def findprimerbyprimername(request):
    if request.POST:
        form = findprimerbyprimernameform(request.POST)
        if form.is_valid():
            #form.save()
            return HttpResponseRedirect('/primer_design/'+str(form.cleaned_data['primername']))
    else:
        findprimer = findprimerbyprimernameform
    
    args={}
    args.update(csrf(request))
    args['findprimer'] = findprimer
    return render_to_response('frontend/findprimerdesignbyprimername.html',args, context_instance=RequestContext(request))

@login_required(login_url='/sorry_login_required/')
def find_primer_design(request):
    args={}
    args.update(csrf(request))
    return render_to_response('frontend/findprimerdesign.html',args, context_instance=RequestContext(request))

def home(request):
    return render_to_response('frontend/home.html')
    

def login(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('frontend/login.html', args, context_instance=RequestContext(request))

def sorry_login_required(request):
    return render_to_response ('frontend/sorry_login_required.html',context_instance=RequestContext(request))

def logout(request):
    auth.logout(request)
    return render_to_response('frontend/logout.html',context_instance=RequestContext(request))


def name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "frontend/name.html", {'form': form})

@login_required(login_url='/sorry_login_required/')
def primer_design(request, primerkey):
    args={}
    args['primerkey']=int(primerkey)
    primerinformation = Primerinformation.objects.all()
    args['primerinformation']=primerinformation
    blattable=Blat.objects.all()
    args['blat']=blattable
    item_strand=Item.objects.all()
    args['item_strand']=item_strand
    snpcheck_table=Snpcheck.objects.all()
    args['snpcheck']=snpcheck_table
    storage_table = Storage.objects.all()
    args['storage']=storage_table
    audit_table=Audit.objects.all()
    args['audit']=audit_table
    pcrproducts_table=Pcrproducts.objects.all()
    args['pcrproducts']=pcrproducts_table
    return render_to_response("frontend/primer_design.html", args,context_instance=RequestContext(request))
    
    return HttpResponseRedirect(reverse(contact_details, args=(new_contact.pk,)))

@login_required(login_url='/sorry_login_required/')
def primer_info(request):
    args = {}
    query_results = Pcrproducts.objects.all()
    args['query_results'] = query_results
    form = ItemForm(request.POST or None)
    args['form'] = form
    
    return render_to_response("frontend/primer_info.html", args,context_instance=RequestContext(request))

def test_output(request):
    # args('list_of_keys')=request.list_of_keys
    return render_to_response('frontend/test_output.html',args,context_instance=RequestContext(request))

def register_success(request):
    return render_to_response('frontend/register_success.html')

def register_user(request):
    if request.method =='POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_success/')

    args={}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    print args
    return render_to_response('frontend/register.html', args,context_instance=RequestContext(request))


# def view1(request):
#     return render_to_response("frontend/view1.html", {'chromosome_list': Chromosome.objects.all()})

@login_required(login_url='/sorry_login_required/')
def welcome(request):
    args={}
    return render_to_response('frontend/welcome.html',context_instance=RequestContext(request))





#def viewprimerdesign(request):

#   There are 11 forms. These are numbered 010, 020 with any subforms named 0101, 0102 etc. The 11 forms are listed below:
# 4.1. To view primer design
# 4.2. To view amplicon(PCR product) design
# 4.3. To add a new primer design
# 4.4. To add a new amplicon design
# 4.5. To edit an existing primer design
# 4.6. To add a new stock tube
# 4.7. To add a new 50uM tube
# 4.8. To add a new 1uM tube
# 4.9. To view the audit trail from a 1uM tube
# 4.10. To view the audit trail from 50uM tube
# 4.11. To view the audit trail from a stock tube.
