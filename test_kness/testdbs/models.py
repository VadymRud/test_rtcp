from django.db import models


class AiDesc(models.Model):

    id_rtu = models.ForeignKey('Rtu',db_column='id_RTU', on_delete=models.CASCADE)  # Field name made lowercase.
    act_v = models.TextField(blank=True, null=True)
    act_t = models.TextField(blank=True, null=True)
    act_q = models.TextField(blank=True, null=True)

    class Meta:

        db_table = 'ai_desc'


class BiDesc(models.Model):

    id_rtu = models.ForeignKey('Rtu', db_column='id_RTU', on_delete=models.CASCADE)  # Field name made lowercase.
    act_v = models.TextField(blank=True, null=True)
    act_t = models.TextField(blank=True, null=True)
    act_q = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'bi_desc'


class Rtu(models.Model):

    url = models.TextField(blank=True, null=True)
    time_upd_int = models.SmallIntegerField()
    class Meta:
        db_table = 'rtu'
