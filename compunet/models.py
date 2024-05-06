from django.db import models


# Create your models here.
class Distribuidor (models.Model):
    nombre= models.CharField(max_length=50)
    direccion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=11)
    email=models.EmailField()
    web=models.URLField()

    def __str__(self):
        return self.nombre 
    
    class Meta:
        verbose_name_plural='Distribuidores'

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    distribuidor=models.ForeignKey(Distribuidor,on_delete=models.CASCADE)
    TIPO=[
        ('Software','Productos de Software'),
        ('Hardware','Productos de Hardware'),
        ('PC','PC`s Armadas'),
        ('Note','Noteboocks'), 
        ('Tablets','Tablets'),
        ]
    tipo=models.CharField(max_length=8,choices=TIPO)
    precio=models.FloatField()
    imagen=models.ImageField(upload_to="imagenes")

    def __str__(self):
        return "%s %s" % (self.nombre,self.marca)

        
