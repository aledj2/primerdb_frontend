from django import forms
from models import Item 

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

# select * from item where ItemCategoryIndex1ID = 55;

class ItemForm(forms.Form):
	version = forms.ChoiceField(choices=Item.objects.filter(itemcategoryindex1id=55).values_list('item','item'))