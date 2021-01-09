from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Roles(models.Model):
    id_rol = models.AutoField(primary_key=True )
    nombre = models.CharField(max_length=25, help_text="Indique el rol")

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.nombre

class Tipo_oleaje(models.Model):
    id_tipo =models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'Tipo de oleaje'
        verbose_name_plural = 'Tipos de oleajes'

class Periodos(models.Model):
    id_periodos = models.AutoField(primary_key=True )
    horario =models.TimeField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = 'Periodo'
        verbose_name_plural = 'Periodos'

class Fase_lunar(models.Model):
    id_fase = models.AutoField(primary_key=True )
    nombre = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'Fase lunar'
        verbose_name_plural = 'Fases lunares'

class Provincias(models.Model):
    id_provincia = models.AutoField(primary_key=True )
    nombre = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'

class Cantones(models.Model):
    id_canton = models.AutoField(primary_key=True )
    nombre = models.CharField(max_length=50)
    id_provincia =models.ForeignKey(Provincias, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cantón'
        verbose_name_plural = 'Cantones'

class Parroquias(models.Model):
    id_parroquia = models.AutoField(primary_key=True )
    nombre = models.CharField(max_length=50)
    id_canton =models.ForeignKey(Cantones, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Parróquia'
        verbose_name_plural = 'Parróquias'

class Estados(models.Model):
    id_estado = models.AutoField(primary_key=True )
    nombre = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

class Estaciones(models.Model):
    id_estacion = models.AutoField(primary_key=True)
    id_parroquia = models.ForeignKey(Parroquias, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    latitud = models.FloatField()
    longitud = models.FloatField()
    puntosReferencia = models.CharField(max_length=100, null=True, blank=True)
    #foto = models.ImageField(max_length=200, blank=True, null=True, upload_to = 'static/img/stations/', default = 'static/img/None/no-img.jpg') 
    foto = models.CharField(max_length=200, null=True)
    id_estado = models.ForeignKey(Estados, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Estación'
        verbose_name_plural = 'Estaciones'

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    auth_user = models.OneToOneField(User, on_delete=models.CASCADE, db_column='auth_user')
    institucion = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    cedula = models.CharField(max_length=15, null=True, blank=True)
    id_provincia = models.ForeignKey(Provincias, on_delete=models.CASCADE)
    id_rol = models.ForeignKey(Roles, on_delete=models.CASCADE)
    id_estado = models.ForeignKey(Estados, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class Observaciones(models.Model):
    id_observacion = models.AutoField(primary_key=True)
    epoca = models.CharField(max_length=15, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    registeredto = models.DateTimeField()
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    id_fase_lunar = models.ForeignKey(Fase_lunar, on_delete=models.CASCADE)
    id_estacion = models.ForeignKey(Estaciones, on_delete=models.CASCADE)
    id_estado = models.ForeignKey(Estados, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Observación'
        verbose_name_plural = 'Observaciones'
        ordering = ["-fecha"]#ordenar por fecha descendente

    

class Mediciones(models.Model):
    id_medicion = models.AutoField(primary_key=True)
    id_observacion = models.ForeignKey(Observaciones, models.DO_NOTHING)
    fechaHora = models.DateTimeField()
    ola_tipo_oleaje = models.ForeignKey(Tipo_oleaje, models.DO_NOTHING)
    corriente_resaca = models.BooleanField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    temperatura = models.FloatField()
    id_periodo = models.ForeignKey(Periodos, models.DO_NOTHING)
    perfil_playa = models.IntegerField()
    ancho_zon_surf = models.FloatField()
    lp_flotador = models.IntegerField()
    lp_rompiente = models.IntegerField()
    crl_espacio = models.FloatField()
    crl_tiempo = models.IntegerField()
    crl_velocidad = models.FloatField()
    crl_direccion = models.CharField(max_length=1)
    vien_direccion = models.IntegerField()
    vien_velocidad = models.FloatField()
    ola_ortogonal = models.IntegerField()
    ola_periodo_onda = models.IntegerField()
    ola_altura_rompiente_promedio = models.FloatField()
    ola_direccion = models.IntegerField()
    estado = models.ForeignKey(Estados, models.DO_NOTHING)

    class Meta:
        verbose_name = 'Medicion'
        verbose_name_plural = 'Mediciones'

class Altura_rompiente(models.Model):
    id_alt_romp = models.AutoField(primary_key=True )
    num_medicion = models.IntegerField()
    valor  = models.FloatField()
    id_medicion = models.ForeignKey(Mediciones, models.DO_NOTHING, db_column='id_medicion')

    class Meta:
        verbose_name = 'Altura rompiente'
        verbose_name_plural = 'Alturas rompientes'