from django.db import models

# Create your models here.
class Stage(models.Model):
    stage = models.IntegerField(
        verbose_name = "Etapa",

    )
    application_date = models.DateField(
        verbose_name = "Fecha de aplicación",
    )

    def month(self):
        months = ['Enero', 'Febrero', 'Marzo', 'April', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octrube', 'Noviembre', 'Diciembre']
        return months[self.application_date.month - 1]

    def year(self):
        return self.application_date.year

    def __str__(self):
        return f"{ self.stage } - { self.month() } { self.year() }"

    class Meta:
        verbose_name = "etapa"
        verbose_name_plural = "etapas"    



        