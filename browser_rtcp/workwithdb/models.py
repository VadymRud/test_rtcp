from __future__ import unicode_literals

from django.db import models


class AiDesc(models.Model):
    id = models.IntegerField(blank=True, null=True)
    id_rtu = models.ForeignKey('Rtu', models.DO_NOTHING, db_column='id_RTU', blank=True, null=True)  # Field name made lowercase.
    act_v = models.TextField(blank=True, null=True)
    act_t = models.TextField(blank=True, null=True)
    act_q = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ai_desc'


class BiDesc(models.Model):
    id = models.IntegerField(blank=True, null=True)
    id_rtu = models.ForeignKey('Rtu', models.DO_NOTHING, db_column='id_RTU', primary_key=True)  # Field name made lowercase.
    act_v = models.TextField(blank=True, null=True)
    act_t = models.TextField(blank=True, null=True)
    act_q = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bi_desc'


class Rtu(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.TextField()
    time_upd_int = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'rtu'
