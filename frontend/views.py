from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Chromosome, Primerinfo, Pcrproducts
from .forms import NameForm, ItemForm

#def home(request):
#    return HttpResponse('Hello World')

def home(request):
    return render_to_response('frontend/home.html')

def chromosome_home(request):
    return render_to_response("frontend/chromosome_home.html", {'chromosome_list': Chromosome.objects.all()})

def chromosome_page(request, pk):
    chromosome = get_object_or_404(Chromosome, pk=pk)
    return render (request, "frontend/chromosome_page.html", {'chromosome':chromosome})

def view1(request):
    return render_to_response("frontend/view1.html", {'chromosome_list': Chromosome.objects.all()})

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

def primer_info(request):
    context = {}
    query_results = Pcrproducts.objects.all()
    context['query_results'] = query_results
    form = ItemForm(request.POST)
    context['form'] = form
    
    return render_to_response("frontend/primer_info.html", context)
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