from django.db import models

# Create your models here.
#Modelo para categoria
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length = 50, verbose_name='Nombre de la Categoria')


    def __str__(self):
        return self.nombreCategoria
    
#Modelo para libro
class Libro(models.Model):
    ISBN = models.CharField(max_length=13, primary_key= True, verbose_name='ISBN')
    nombreLibro = models.CharField(max_length=30, verbose_name='Nombre de libro')
    autor = models.CharField(max_length=20, null= True, verbose_name='Autor')
    Descripcion = models.CharField(max_length=200,verbose_name='descripcion')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__(self):
        return self.ISBN
    