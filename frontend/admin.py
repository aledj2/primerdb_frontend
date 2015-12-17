from django.contrib import admin
from .models import Item
from .models import Audit
from .models import Blat
from .models import Chromosome
from .models import Geneshgnc140714
from .models import GenesrefseqHg19
from .models import Gsmamplicons
from .models import Itemcategory
from .models import Manipulateblatinfo
from .models import Modifications
from .models import Pcrproducts
from .models import Primerinfo
from .models import Primerinformation
from .models import Snpcheck
from .models import Storage

admin.site.register(Item)
admin.site.register(Audit)
admin.site.register(Blat)
admin.site.register(Chromosome)
admin.site.register(Geneshgnc140714)
admin.site.register(GenesrefseqHg19)
admin.site.register(Gsmamplicons)
admin.site.register(Itemcategory)
admin.site.register(Manipulateblatinfo)
admin.site.register(Modifications)
admin.site.register(Pcrproducts)
admin.site.register(Primerinfo)
admin.site.register(Primerinformation)
admin.site.register(Snpcheck)
admin.site.register(Storage)