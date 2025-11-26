from django.db import models

class Cliente(models.Model):
    codigo = models.CharField(max_length=10, unique=True, verbose_name="Código Cliente")
    nombre = models.CharField(max_length=100, verbose_name="Nombre / Razón Social")
    direccion = models.CharField(max_length=200, blank=True, null=True)
    cod_postal = models.CharField(max_length=10, blank=True, null=True)
    localidad = models.CharField(max_length=100, blank=True, null=True)
    provincia = models.CharField(max_length=50, blank=True, null=True)
    cuit = models.CharField(max_length=13, unique=True, verbose_name="CUIT")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['nombre']