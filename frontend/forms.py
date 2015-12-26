from django import forms
from models import Chromosome, Primerinformation, Pcrproducts, Blat, Item, Geneshgnc140714, Snpcheck, Storage, Audit
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import operator
from datetime import date

# Add new primer wizard
class add_new_primer1(forms.Form):
	gene = forms.TypedChoiceField(choices=Geneshgnc140714.objects.values_list('geneshgncid','approvedsymbol').filter(used__gte=0).order_by('-used','approvedsymbol'))
	exon = forms.IntegerField()

class add_new_primer2(forms.Form):
	tag = forms.ChoiceField(choices=Item.objects.filter(itemcategoryindex1id=54).values_list('itemid','item'))
	sequence = forms.CharField()
	chromosome = forms.ChoiceField(choices=Chromosome.objects.filter(sorting__gte=100).filter(sorting__lte=125).values_list('chrid','chr'))
	start = forms.IntegerField()	
	stop = forms.IntegerField()	
	strand = forms.ChoiceField(choices=Item.objects.filter(itemcategoryindex1id=52).values_list('itemid','item'))
	genomebuild = forms.ChoiceField(choices=Item.objects.filter(itemcategoryindex1id=64).values_list('itemid','item'))
	concentration = forms.ChoiceField(choices=Item.objects.filter(itemcategoryindex1id=53).filter(itemcategoryindex2id=1).values_list('itemid','item').order_by('-item'))

class add_new_primer3(forms.Form):
	snpchecked = forms.ChoiceField(choices=Item.objects.filter(itemcategoryindex1id=60).values_list('itemid','item'))
	dateofsnpcheck = forms.DateField(label='Date of SNP check (format YYYY-MM-DD) ', input_formats=['%Y-%m-%d'], required=False) 
	result = forms.ChoiceField(choices=Item.objects.filter(itemcategoryindex1id=62).values_list('itemid','item'))
	dbbuild = forms.IntegerField(required=False)
	nt = forms.CharField(required=False)
	rs1 = forms.CharField(required=False)
	rs2 = forms.CharField(required=False)
	rs3 = forms.CharField(required=False)
	validated = forms.CharField(required=False)

class add_new_primer4(forms.Form):
	assay = forms.ChoiceField(choices=Item.objects.filter(itemcategoryindex1id=58).values_list('itemid','item'))
	pcrprogram = forms.CharField(required=False)
	pcrconditions = forms.CharField(required=False)
	ucsc = forms.CharField(required=False)
	notes = forms.CharField(required=False)

class add_new_primer_summary(forms.Form):
	pass

class approvedsymbollist(forms.Form):
	 gene_symbol_list = forms.TypedChoiceField(choices=Geneshgnc140714.objects.values_list('geneshgncid','approvedsymbol').order_by('-used','approvedsymbol'))
	 exon = forms.IntegerField()
	 tag = forms.TypedChoiceField(choices=Item.objects.filter(itemcategoryindex1id=54).values_list('item','item'))


class findampliconbygene_selectgene(forms.Form):
	gene = forms.TypedChoiceField(label = "select gene",widget=forms.Select(), choices=Geneshgnc140714.objects.values_list('geneshgncid','approvedsymbol').filter(used__gte=1).order_by('approvedsymbol'))

class findampliconbygene_selectexon(forms.Form):
	def __init__(self, geneid, *args, **kwargs):
		geneid=kwargs.pop('geneid',None)
		super(findampliconbygene_selectexon, self).__init__(*args, **kwargs)
		
	exon = forms.ChoiceField(label = "select exon", choices=Primerinformation.objects.values_list('exon','exon').distinct())
	



class findprimerform(forms.ModelForm):
	class Meta:
		model=Primerinformation
		fields=['primername', 'exon']

class findprimerbycoordform(forms.Form):
	chromosome = forms.ChoiceField(choices=Chromosome.objects.filter(sorting__gte=100).filter(sorting__lte=125).values_list('chrid','chr'))
	position = forms.IntegerField()	
	

class findprimerbygene_selectgene(forms.Form):
	gene = forms.TypedChoiceField(label = "select gene",widget=forms.Select(), choices=Geneshgnc140714.objects.values_list('geneshgncid','approvedsymbol').filter(used__gte=1).order_by('approvedsymbol'))

class findprimerbygene_selectexon(forms.Form):
	def __init__(self, geneid, *args, **kwargs):
		geneid=kwargs.pop('geneid',None)
		super(findprimerbygene_selectexon, self).__init__(*args, **kwargs)
		
	exon = forms.ChoiceField(label = "select exon", choices=Primerinformation.objects.values_list('exon','exon').distinct())
	
class findprimerbyprimernameform(forms.Form):
	primername = forms.TypedChoiceField(label="primername",choices=Primerinformation.objects.values_list('primerkey','primername'))

class ItemForm(forms.Form):
	version = forms.TypedChoiceField(choices=Item.objects.filter(itemcategoryindex1id=55).values_list('item','item'))
	Genesymbol = forms.TypedChoiceField(choices=Geneshgnc140714.objects.values_list('approvedsymbol','approvedsymbol'))

class MyRegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	
	class Meta:
		model = User
		fields = ('username','email','first_name','last_name','password1','password2')

	def save(self, commit=True):
		user = super(MyRegistrationForm, self).save(commit=False)
		user.email=self.cleaned_data['email']
		user.first_name=self.cleaned_data['first_name']
		user.last_name=self.cleaned_data['last_name']
		
		if commit:
			user.save()
		return user


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class Newprimerdesign_primerinformation(forms.ModelForm):
	class Meta:
		model = Primerinformation
		#Gene_symbol = forms.ChoiceField(choices=Geneshgnc140714.objects.values_list('geneshgncid','approvedsymbol'))
		fields = ['exon','sequence']

class Newprimerdesign_snpcheck(forms.ModelForm):
	class Meta:
		model=Snpcheck
		fields='__all__'
