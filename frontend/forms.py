from django import forms
from models import Chromosome, Primerinformation, Pcrproducts, Blat, Item, Geneshgnc140714, Snpcheck, Storage, Audit
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class approvedsymbollist(forms.Form):
	gene_symbol_list = forms.ChoiceField(choices=Geneshgnc140714.objects.values_list('geneshgncid','approvedsymbol'))

class findprimerform(forms.ModelForm):
	class Meta:
		model=Primerinformation
		fields=['primername', 'exon']

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
