# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class Huinya(models.Model):
    act_t = models.TextField(blank=True, null=True)
    act_q = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'huinya'
#
#
# class BiDesc(models.Model):
#     id = models.IntegerField(blank=True, null=True)
#     id_rtu = models.OneToOneField('Rtu', models.DO_NOTHING, db_column='id_RTU', primary_key=True)  # Field name made lowercase.
#     act_v = models.TextField(blank=True, null=True)
#     act_t = models.TextField(blank=True, null=True)
#     act_q = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bi_desc'
#
#
# class Rtu(models.Model):
#     id = models.IntegerField(primary_key=True)
#     url = models.TextField()
#     time_upd_int = models.SmallIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'rtu'
