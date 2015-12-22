import autocomplete_light
from models import Geneshgnc140714

autocomplete_light.register(Geneshgnc140714, search_fields=('approved_symbol',), autocomplete_js_attributes={'data-autocomplete-minimum-characters': 1})