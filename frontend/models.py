# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.db import models


class Audit(models.Model):
    auditkey = models.AutoField(db_column='AuditKey', primary_key=True)  # Field name made lowercase.
    storagekey = models.IntegerField(db_column='StorageKey')  # Field name made lowercase.
    datemade = models.CharField(db_column='DateMade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    supplier = models.IntegerField(db_column='Supplier', blank=True, null=True)  # Field name made lowercase.
    productcode = models.CharField(db_column='ProductCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.CharField(db_column='ExpiryDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    batchnumber = models.CharField(db_column='BatchNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    oligonumber = models.CharField(db_column='OligoNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shipmentdate = models.CharField(db_column='ShipmentDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datereceived = models.DateField(db_column='DateReceived', blank=True, null=True)  # Field name made lowercase.
    fprimerauditkey = models.IntegerField(db_column='FPrimerAuditKey', blank=True, null=True)  # Field name made lowercase.
    rprimerauditkey = models.IntegerField(db_column='RPrimerAuditKey', blank=True, null=True)  # Field name made lowercase.
    dilutionauditkey = models.IntegerField(db_column='DilutionAuditKey', blank=True, null=True)  # Field name made lowercase.
    teh2olot = models.CharField(db_column='TEH2OLot', max_length=50, blank=True, null=True)  # Field name made lowercase.
    madeby = models.IntegerField(db_column='MadeBy', blank=True, null=True)  # Field name made lowercase.
    
    def supplier_txt(self):
        return Item.objects.get(itemid=self.supplier)
        
    def madeby_txt(self):
        return Item.objects.get(itemid=self.madeby)


    def __unicode__(self):
        return str(self.auditkey)
    
    class Meta:
        managed = False
        db_table = 'audit'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.ForeignKey(AuthGroup)
    permission_id = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.ForeignKey(AuthUser)
    group_id = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.ForeignKey(AuthUser)
    permission_id = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Blat(models.Model):
    blatkey = models.AutoField(db_column='BlatKey', primary_key=True)  # Field name made lowercase.
    primerkey = models.IntegerField(db_column='PrimerKey')  # Field name made lowercase.
    strand = models.IntegerField(db_column='Strand', blank=True, null=True)  # Field name made lowercase.
    start = models.IntegerField(db_column='Start', blank=True, null=True)  # Field name made lowercase.
    stop = models.IntegerField(db_column='Stop', blank=True, null=True)  # Field name made lowercase.
    genomebuild = models.CharField(db_column='GenomeBuild', max_length=50, blank=True, null=True)  # Field name made lowercase.
    
    def strandtxt(self):
        return Item.objects.get(itemid=self.strand)
        
    def genomebuild_txt(self):
        return Item.objects.get(itemid=self.genomebuild)

    def __unicode__(self):
        return str(self.blatkey)

    class Meta:
        managed = False
        db_table = 'blat'


class Chromosome(models.Model):
    chrid = models.IntegerField(db_column='ChrID', primary_key=True)  # Field name made lowercase.
    chr = models.CharField(db_column='Chr', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chromosome = models.FloatField(db_column='Chromosome', blank=True, null=True)  # Field name made lowercase.
    size = models.FloatField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    sorting = models.IntegerField(db_column='Sorting', blank=True, null=True)  # Field name made lowercase.
    def __unicode__(self):
        return str(self.chrid)
    class Meta:
        managed = False
        db_table = 'chromosome'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Geneshgnc140714(models.Model):
    geneshgncid = models.IntegerField(db_column='GenesHGNCID', primary_key=True)  # Field name made lowercase.
    hgncid = models.CharField(db_column='HGNCID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approvedsymbol = models.CharField(db_column='ApprovedSymbol', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approvedname = models.CharField(db_column='ApprovedName', max_length=750, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locustype = models.CharField(db_column='LocusType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    locusgroup = models.CharField(db_column='LocusGroup', max_length=255, blank=True, null=True)  # Field name made lowercase.
    previoussymbols = models.CharField(db_column='PreviousSymbols', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    previousnames = models.CharField(db_column='PreviousNames', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    synonyms = models.CharField(db_column='Synonyms', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    namesynonyms = models.CharField(db_column='NameSynonyms', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    chromosome = models.CharField(db_column='Chromosome', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dateapproved = models.DateTimeField(db_column='DateApproved', blank=True, null=True)  # Field name made lowercase.
    datemodified = models.DateTimeField(db_column='DateModified', blank=True, null=True)  # Field name made lowercase.
    accessionnumbers = models.CharField(db_column='AccessionNumbers', max_length=255, blank=True, null=True)  # Field name made lowercase.
    specialistdatabaselinks = models.CharField(db_column='SpecialistDatabaseLinks', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    specialistdatabaseids = models.CharField(db_column='SpecialistDatabaseIDs', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    genefamilytag = models.CharField(db_column='GeneFamilyTag', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    genefamilydescription = models.CharField(db_column='GeneFamilyDescription', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    locusspecificdatabases = models.CharField(db_column='LocusSpecificDatabases', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    entrezgeneidmapped = models.IntegerField(db_column='EntrezGeneIDmapped', blank=True, null=True)  # Field name made lowercase.
    omimidmapped = models.IntegerField(db_column='OMIMIDmapped', blank=True, null=True)  # Field name made lowercase.
    refseqmapped = models.CharField(db_column='RefSeqmapped', max_length=50, blank=True, null=True)  # Field name made lowercase.
    uniprotidmapped = models.CharField(db_column='UniProtIDmapped', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ensemblidmapped = models.CharField(db_column='EnsemblIDmapped', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ucscidmapped = models.CharField(db_column='UCSCIDmapped', max_length=50, blank=True, null=True)  # Field name made lowercase.
    refseqguys = models.CharField(db_column='RefSeqGuys', max_length=50, blank=True, null=True)  # Field name made lowercase.
    refseqguysupdated = models.DateTimeField(db_column='RefSeqGuysUpdated', blank=True, null=True)  # Field name made lowercase.
    def __unicode__(self):
        return str(self.geneshgncid)
    class Meta:
        managed = False
        db_table = 'geneshgnc_140714'


class GenesrefseqHg19(models.Model):
    genesrefseq_hg19id = models.IntegerField(db_column='GenesRefSeq_hg19ID')  # Field name made lowercase.
    chrid = models.IntegerField(db_column='ChrID', blank=True, null=True)  # Field name made lowercase.
    strand = models.CharField(db_column='Strand', max_length=50, blank=True, null=True)  # Field name made lowercase.
    start = models.IntegerField(db_column='Start', blank=True, null=True)  # Field name made lowercase.
    stop = models.IntegerField(db_column='Stop', blank=True, null=True)  # Field name made lowercase.
    geneid = models.IntegerField(db_column='GeneID', blank=True, null=True)  # Field name made lowercase.
    def __unicode__(self):
        return str(self.genesrefseq_hg19id)
    class Meta:
        managed = False
        db_table = 'genesrefseq_hg19'


class Gsmamplicons(models.Model):
    gsm_amplicon_key = models.AutoField(db_column='GSM_AMPLICON_KEY', primary_key=True)  # Field name made lowercase.
    amplicon_id = models.IntegerField(db_column='Amplicon_ID', blank=True, null=True)  # Field name made lowercase.
    amplicon_name = models.CharField(db_column='Amplicon_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    amplicon_name_modified = models.CharField(db_column='Amplicon_Name_modified', max_length=50, blank=True, null=True)  # Field name made lowercase.
    exon = models.CharField(db_column='Exon', max_length=50, blank=True, null=True)  # Field name made lowercase.
    def __unicode__(self):
        return str(self.gsm_amplicon_key)

    class Meta:
        managed = False
        db_table = 'gsmamplicons'


class Item(models.Model):
    itemid = models.AutoField(db_column='ItemID', primary_key=True)  # Field name made lowercase.
    item = models.CharField(db_column='Item', max_length=255, blank=True, null=True)  # Field name made lowercase.
    itemcategoryindex1id = models.IntegerField(db_column='ItemCategoryIndex1ID', blank=True, null=True)  # Field name made lowercase.
    itemcategoryindex2id = models.IntegerField(db_column='ItemCategoryIndex2ID', blank=True, null=True)  # Field name made lowercase.
    itemcategoryindex3id = models.IntegerField(db_column='ItemCategoryIndex3ID', blank=True, null=True)  # Field name made lowercase.
    itemcategoryindex4id = models.IntegerField(db_column='ItemCategoryIndex4ID', blank=True, null=True)  # Field name made lowercase.
    sorting = models.IntegerField(db_column='Sorting', blank=True, null=True)  # Field name made lowercase.
    abbreviated = models.CharField(db_column='Abbreviated', max_length=50, blank=True, null=True)  # Field name made lowercase.
    
    def __unicode__(self):
        return str(self.itemid)

    class Meta:
        managed = False
        db_table = 'item'


class Itemcategory(models.Model):
    itemcategoryid = models.AutoField(db_column='ItemCategoryID', primary_key=True)  # Field name made lowercase.
    itemcategory = models.CharField(db_column='ItemCategory', max_length=255, blank=True, null=True)  # Field name made lowercase.
    categoryindex = models.IntegerField(db_column='CategoryIndex', blank=True, null=True)  # Field name made lowercase.
    def __unicode__(self):
        return str(self.itemcategoryid)
    class Meta:
        managed = False
        db_table = 'itemcategory'


class Manipulateblatinfo(models.Model):
    match = models.IntegerField(db_column='Match', blank=True, null=True)  # Field name made lowercase.
    mismatch = models.IntegerField(db_column='Mismatch', blank=True, null=True)  # Field name made lowercase.
    repmatches = models.IntegerField(db_column='RepMatches', blank=True, null=True)  # Field name made lowercase.
    ncount = models.IntegerField(db_column='nCount', blank=True, null=True)  # Field name made lowercase.
    qnuminsert = models.IntegerField(db_column='qNumInsert', blank=True, null=True)  # Field name made lowercase.
    qbaseinsert = models.IntegerField(db_column='qBaseInsert', blank=True, null=True)  # Field name made lowercase.
    tnuminsert = models.IntegerField(db_column='tNumInsert', blank=True, null=True)  # Field name made lowercase.
    tbaseinsert = models.IntegerField(db_column='tBaseInsert', blank=True, null=True)  # Field name made lowercase.
    strand = models.CharField(db_column='Strand', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qname = models.CharField(db_column='qName', primary_key=True, max_length=50)  # Field name made lowercase.
    qsize = models.IntegerField(db_column='qSize', blank=True, null=True)  # Field name made lowercase.
    qstart = models.IntegerField(db_column='qStart', blank=True, null=True)  # Field name made lowercase.
    qend = models.IntegerField(db_column='qEnd', blank=True, null=True)  # Field name made lowercase.
    tname = models.CharField(db_column='tName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tsize = models.IntegerField(db_column='tSize', blank=True, null=True)  # Field name made lowercase.
    tstart = models.IntegerField(db_column='tStart', blank=True, null=True)  # Field name made lowercase.
    tend = models.IntegerField(db_column='tEnd', blank=True, null=True)  # Field name made lowercase.
    blockcount = models.IntegerField(db_column='BlockCount', blank=True, null=True)  # Field name made lowercase.
    blocksizes = models.CharField(db_column='BlockSizes', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qstarts = models.CharField(db_column='qStarts', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tstarts = models.CharField(db_column='tStarts', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tsearchchr = models.CharField(db_column='tsearchChr', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tsearchstart = models.IntegerField(db_column='tsearchStart', blank=True, null=True)  # Field name made lowercase.
    tsearchstop = models.IntegerField(db_column='tsearchStop', blank=True, null=True)  # Field name made lowercase.
    primerstart = models.IntegerField(db_column='PrimerStart', blank=True, null=True)  # Field name made lowercase.
    primerstop = models.IntegerField(db_column='PrimerStop', blank=True, null=True)  # Field name made lowercase.
    def __unicode__(self):
        return str(self.match)
    class Meta:
        managed = False
        db_table = 'manipulateblatinfo'


class Modifications(models.Model):
    tablekey = models.AutoField(db_column='TableKey', primary_key=True)  # Field name made lowercase.
    tagsequence = models.CharField(db_column='TagSequence', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tagname = models.IntegerField(db_column='TagName', blank=True, null=True)  # Field name made lowercase.
    def __unicode__(self):
        return str(self.tablekey)
    class Meta:
        managed = False
        db_table = 'modifications'


class Pcrproducts(models.Model):
    productkey = models.AutoField(db_column='ProductKey', primary_key=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fprimerid = models.IntegerField(db_column='FPrimerID', blank=True, null=True)  # Field name made lowercase.
    rprimerid = models.IntegerField(db_column='RPrimerID', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=500)  # Field name made lowercase.
    active = models.TextField(db_column='Active')  # Field name made lowercase. This field type is a guess.
    def __unicode__(self):
        return str(self.productkey)

    def pcrproducts_version_txt (self):
        return Item.objects.get(itemid=self.version)
        
    class Meta:
        managed = False
        db_table = 'pcrproducts'


class Primerinfo(models.Model):
    gene = models.CharField(db_column='Gene', max_length=50, blank=True, null=True)  # Field name made lowercase.
    exonfragment = models.CharField(db_column='ExonFragment', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chromosome = models.CharField(db_column='Chromosome', max_length=50, blank=True, null=True)  # Field name made lowercase.
    primernameconc = models.CharField(db_column='PrimerNameConc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    primername = models.CharField(db_column='PrimerName', primary_key=True, max_length=100)  # Field name made lowercase.
    newname = models.CharField(db_column='NewName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    primerseq = models.CharField(db_column='Primerseq', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pcrprog = models.CharField(db_column='PCRProg', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pcrcond = models.CharField(db_column='PCRCond', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modification = models.CharField(db_column='Modification', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ampliconsize = models.CharField(db_column='AmpliconSize', max_length=50, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stockconc = models.CharField(db_column='StockConc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tray = models.CharField(db_column='Tray', max_length=50, blank=True, null=True)  # Field name made lowercase.
    grid1 = models.CharField(db_column='GRID1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    grid2 = models.CharField(db_column='GRID2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    grid3 = models.CharField(db_column='GRID3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    grid4 = models.CharField(db_column='GRID4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    grid5 = models.CharField(db_column='GRID5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    grid6 = models.CharField(db_column='GRID6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    grid7 = models.CharField(db_column='GRID7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    grid8 = models.CharField(db_column='GRID8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    grid9 = models.CharField(db_column='GRID9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    grid10 = models.CharField(db_column='GRID10', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gridcomb = models.CharField(db_column='GRIDCOMB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    supplier = models.CharField(db_column='Supplier', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datemade = models.CharField(db_column='DateMade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    productcode = models.CharField(db_column='ProductCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.CharField(db_column='ExpiryDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    batchnumber = models.CharField(db_column='BatchNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    oligono = models.CharField(db_column='OligoNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shipmentdate = models.CharField(db_column='ShipmentDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    snpchecked = models.CharField(db_column='SNPChecked', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dateofsnpcheck = models.CharField(db_column='DateOfSNPCheck', max_length=50, blank=True, null=True)  # Field name made lowercase.
    snpdbbuild = models.CharField(db_column='SNPdbBuild', max_length=50, blank=True, null=True)  # Field name made lowercase.
    snpresult = models.CharField(db_column='SNPResult', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assay = models.CharField(db_column='Assay', max_length=100, blank=True, null=True)  # Field name made lowercase.
    correctprimerinlab = models.CharField(db_column='CorrectPrimerInLab', max_length=50, blank=True, null=True)  # Field name made lowercase.
    listsandgsmupdated = models.CharField(db_column='ListsandGSMUpdated', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ucsc = models.CharField(db_column='UCSC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nt = models.CharField(db_column='NT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=300, blank=True, null=True)  # Field name made lowercase.
    primersvalidated = models.CharField(db_column='PrimersValidated', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rs = models.CharField(db_column='RS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    strand = models.CharField(db_column='Strand', max_length=50, blank=True, null=True)  # Field name made lowercase.
    start = models.CharField(db_column='Start', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stop = models.CharField(db_column='Stop', max_length=50, blank=True, null=True)  # Field name made lowercase.
    

    
    def __unicode__(self):
        return str(self.gene)
    class Meta:
        managed = False
        db_table = 'primerinfo'


class Primerinformation(models.Model):
    primerkey = models.AutoField(db_column='PrimerKey', primary_key=True)  # Field name made lowercase.
    geneshgncid = models.IntegerField(db_column='GenesHGNCID', blank=True, null=True)  # Field name made lowercase.
    exon = models.CharField(db_column='Exon', max_length=50, blank=True, null=True)  # Field name made lowercase.
    exon_2 = models.CharField(db_column='Exon_2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chromosome = models.IntegerField(db_column='Chromosome', blank=True, null=True)  # Field name made lowercase.
    primername = models.CharField(db_column='PrimerName', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    sequence = models.CharField(db_column='Sequence', max_length=75, blank=True, null=True)  # Field name made lowercase.
    modification = models.IntegerField(db_column='Modification', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.
    pcrconditions = models.CharField(db_column='PCRConditions', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pcrprogram = models.CharField(db_column='PCRProgram', max_length=500, blank=True, null=True)  # Field name made lowercase.
    assay = models.IntegerField(db_column='Assay', blank=True, null=True)  # Field name made lowercase.
    ucsc = models.CharField(db_column='UCSC', max_length=500, blank=True, null=True)  # Field name made lowercase.
    
    def gene_symbol(self):
        return Geneshgnc140714.objects.get(geneshgncid=self.geneshgncid)
    
    def chromosome_table(self):
        return Chromosome.objects.get(chrid=self.chromosome)
    
    def start_stop(self):
        return Blat.objects.get(primerkey=self.primerkey)
    
    def snpcheck (self):
        return Snpcheck.objects.get(primerkey=self.primerkey)
    
    def version_text (self):
        return Item.objects.get(itemid=self.version)

    def modification_text (self):
        return Item.objects.get(itemid=self.modification)

    def assay_txt (self):
        return Item.objects.get(itemid=self.assay)
    
    def __unicode__(self):
        return str(self.primerkey)
    
    class Meta:
        managed = False
        db_table = 'primerinformation'


class Snpcheck(models.Model):
    snpcheckkey = models.AutoField(db_column='SNPCheckKey', primary_key=True)  # Field name made lowercase.
    primerkey = models.IntegerField(db_column='PrimerKey')  # Field name made lowercase.
    result = models.IntegerField(db_column='Result', blank=True, null=True)  # Field name made lowercase.
    snpchecked = models.IntegerField(db_column='SNPChecked', blank=True, null=True)  # Field name made lowercase.
    dateofsnpcheck = models.CharField(db_column='DateofSNPCheck', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dbbuild = models.CharField(db_column='dbBuild', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rs1 = models.CharField(db_column='RS1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rs2 = models.CharField(db_column='RS2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rs3 = models.CharField(db_column='RS3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nt = models.CharField(db_column='NT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=500, blank=True, null=True)  # Field name made lowercase.
    validated = models.CharField(db_column='Validated', max_length=100, blank=True, null=True)  # Field name made lowercase.
    datestamp = models.DateTimeField(db_column='DateStamp', blank=True, null=True)  # Field name made lowercase.
    
    def snpcheck_result_txt(self):
        return Item.objects.get(itemid=self.result)
        
    def snpchecked_txt(self):
        return Item.objects.get(itemid=self.snpchecked)

    def __unicode__(self):
        return str(self.snpcheckkey)
    class Meta:
        managed = False
        db_table = 'snpcheck'


class Storage(models.Model):
    storagekey = models.AutoField(db_column='StorageKey', primary_key=True)  # Field name made lowercase.
    primerkey = models.IntegerField(db_column='PrimerKey', blank=True, null=True)  # Field name made lowercase.
    tray = models.IntegerField(db_column='Tray', blank=True, null=True)  # Field name made lowercase.
    grid = models.IntegerField(db_column='Grid')  # Field name made lowercase.
    pcrproductkey = models.IntegerField(db_column='PCRProductKey', blank=True, null=True)  # Field name made lowercase.
    active = models.TextField(db_column='Active')  # Field name made lowercase. This field type is a guess.
    concentration = models.IntegerField(db_column='Concentration', blank=True, null=True)  # Field name made lowercase.
    
    def storage_tray_txt(self):
        return Item.objects.get(itemid=self.tray)
        
    def storage_grid_txt(self):
        return Item.objects.get(itemid=self.grid)

    def storage_conc_txt(self):
        return Item.objects.get(itemid=self.concentration)        

    def __unicode__(self):
        return str(self.storagekey)
    class Meta:
        managed = False
        db_table = 'storage'
