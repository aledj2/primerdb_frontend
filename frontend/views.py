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
from .models import Chromosome, Primerinformation, Pcrproducts, Primerinfo, Blat, Item, Geneshgnc140714, Snpcheck, Storage, Audit
from .forms import *
from formtools.wizard.views import SessionWizardView

# @login_required(login_url='/sorry_login_required/')
# def add_primer_design(request):
#     addprimer={}
#     if request.POST:
#         form = NewPrimerdesign(request.POST)
#         if form.is_valid():
#             request.session()
#             return HttpResponseRedirect('/primerinformation/')
#     else:
#         Newprimerdesign_primerinformation_form = Newprimerdesign_primerinformation
    
#     args={}
#     args.update(csrf(request))
#     args['Newprimerdesign_primerinformation'] = Newprimerdesign_primerinformation_form
#     Newprimerdesign_snpcheck_form=Newprimerdesign_snpcheck
#     args['Newprimerdesign_snpcheck'] = Newprimerdesign_snpcheck_form
#     list_of_genes=approvedsymbollist
#     args['approvedsymbollist']=list_of_genes
    
#     return render_to_response('frontend/addprimerdesign.html',args,context_instance=RequestContext(request))

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

        #gene['list_of_data']=list_of_data
        # args={}
        # args('list_of_keys')=list_of_keys

        #     if key =="gene":
        #         gene=form_dict[key]
        
        if gene is not None:
            primer=Primerinformation(geneshgncid=gene, exon=exon,exon_2=exon2,sequence=sequence,chromosome=chrom,modification=mod)
            commit=True

        if commit:
            primer.save()
            primer.primerkey
        
        return HttpResponse(primer.primerkey)


@login_required(login_url='/sorry_login_required/')
def amplicon_design(request):
    args={}
    productid = 1
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

# def chromosome_home(request):
#     return render_to_response("frontend/chromosome_home.html", {'chromosome_list': Chromosome.objects.all()})

# def chromosome_page(request, pk):
#     chromosome = get_object_or_404(Chromosome, pk=pk)
#     return render (request, "frontend/chromosome_page.html", {'chromosome':chromosome})

@login_required(login_url='/sorry_login_required/')
def find_primer_design(request):
    if request.POST:
        form = findprimerform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/primerinformation/')
    else:
        findprimer = findprimerform
    
    args={}
    args.update(csrf(request))
    args['findprimerform'] = findprimer
    return render_to_response('frontend/viewprimerdesign.html',args,context_instance=RequestContext(request))

# def home(request):
#     return render_to_response('frontend/home.html')
    

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('frontend/login.html', c,context_instance=RequestContext(request))

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
def primer_design(request,primerid):
    args={}
    primerid = primerid
    args['pid']=primername
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
