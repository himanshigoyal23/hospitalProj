from django.db import models

# Create your models here.
class Hospbeds(models.Model):
    totalbeds = models.IntegerField(db_column='totalBeds', max_digits=65535, blank=True, null=True)  # Field name made lowercase.
    hospitalid = models.CharField(db_column='hospitalId', primary_key=True, max_length=20)  # Field name made lowercase.
    ncv = models.IntegerField(max_digits=65535, blank=True, null=True)
    nco = models.IntegerField(max_digits=65535, blank=True, null=True)
    nci = models.IntegerField(max_digits=65535, blank=True, null=True)
    cvv = models.IntegerField(max_digits=65535, blank=True, null=True)
    cov = models.IntegerField(max_digits=65535, blank=True, null=True)
    civ = models.IntegerField(max_digits=65535, blank=True, null=True)
    cvr = models.IntegerField(max_digits=65535, blank=True, null=True)
    cor = models.IntegerField(max_digits=65535, blank=True, null=True)
    cir = models.IntegerField(max_digits=65535, blank=True, null=True)
    cvo = models.IntegerField(max_digits=65535, blank=True, null=True)
    coo = models.IntegerField(max_digits=65535, blank=True, null=True)
    cio = models.IntegerField(max_digits=65535, blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HospBeds'