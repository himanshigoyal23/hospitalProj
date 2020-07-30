from django.db import models
from django.contrib.gis.db import models
# Create your models here.
class Hospbeds(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.PointField(blank=True, null=True)
    factly_nam = models.CharField(max_length=254, blank=True, null=True)
    totalbeds = models.BigIntegerField(blank=True, null=True)
    ncv = models.BigIntegerField(blank=True, null=True)
    nco = models.BigIntegerField(blank=True, null=True)
    nci = models.BigIntegerField(blank=True, null=True)
    cvv = models.BigIntegerField(blank=True, null=True)
    cov = models.BigIntegerField(blank=True, null=True)
    civ = models.BigIntegerField(blank=True, null=True)
    cvr = models.BigIntegerField(blank=True, null=True)
    cor = models.BigIntegerField(blank=True, null=True)
    cir = models.BigIntegerField(blank=True, null=True)
    cvo = models.BigIntegerField(blank=True, null=True)
    coo = models.BigIntegerField(blank=True, null=True)
    cio = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HospBeds'
# class Hospbeds(models.Model):
#     totalbeds = models.IntegerField(db_column='totalBeds',  blank=True, null=True)  # Field name made lowercase.
#     hospitalid = models.CharField(db_column='hospitalId', primary_key=True, max_length=20)  # Field name made lowercase.
#     ncv = models.IntegerField( blank=True, null=True)
#     nco = models.IntegerField( blank=True, null=True)
#     nci = models.IntegerField( blank=True, null=True)
#     cvv = models.IntegerField( blank=True, null=True)
#     cov = models.IntegerField( blank=True, null=True)
#     civ = models.IntegerField( blank=True, null=True)
#     cvr = models.IntegerField( blank=True, null=True)
#     cor = models.IntegerField( blank=True, null=True)
#     cir = models.IntegerField( blank=True, null=True)
#     cvo = models.IntegerField( blank=True, null=True)
#     coo = models.IntegerField( blank=True, null=True)
#     cio = models.IntegerField( blank=True, null=True)
#     geom = models.PointField(blank=True, null=True)

#     class Meta:
#         managed = False
        # db_table = 'HospBeds'