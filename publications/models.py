from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name="usuario")
    #avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    # Para el campo tipo imagen hay que tener Pillow en el entorno virtual y configurar el servidor para servir archivos media.(settings.py).74
    bio = models.TextField(verbose_name="bio", null=True, blank=True)
    link = models.URLField(verbose_name="link", max_length=200, null=True, blank=True)

    
    class Meta:
        ordering = ['user__username'] 
        verbose_name = "perfil"
        verbose_name_plural = "perfiles"

    def __str__(self):
        return self.user.username


class Location(models.Model):

    name = models.CharField(verbose_name="nombre", max_length=50)

    class Meta:
        verbose_name = "localidad"
        verbose_name_plural = "localidades"

    def __str__(self):
        return self.name

class Breed(models.Model):

    name = models.CharField(verbose_name="nombre", max_length=50)

    class Meta:
        verbose_name = "raza"
        verbose_name_plural = "razas"

    def __str__(self):
        return self.name
    

class PetMixin(models.Model):

    class Meta:
        abstract = True

    ANIMAL_CHOICES = (
        ('PE','Perro/s'),
        ('GA','Gato/s')
    )
    GENDER_CHOICES = (
        ('HE','Hembra'),
        ('MA','Macho'),
        ('NO','No Sabe')
    )
    AGE_CHOICES = (
        ('CA','Cachorro'),
        ('JO', 'Joven'),
        ('AD','Adulto'),
        ('VI', 'Viejo')
    )
    SIZE_CHOICES = (
        ('CH','Chico'),
        ('CM','Chico/Mediano'),
        ('ME','Mediano'),
        ('GR','Grande')
    )

    profile = models.ForeignKey(Profile, verbose_name="perfil", on_delete=models.CASCADE)
    animal = models.CharField(verbose_name="animal", max_length=2, choices=ANIMAL_CHOICES)
    genere = models.CharField(verbose_name="genero", max_length=2, choices=GENDER_CHOICES)
    age = models.CharField(verbose_name="edad", max_length=2, choices=AGE_CHOICES)
    size = models.CharField(verbose_name="tamaño", max_length=2, choices=SIZE_CHOICES)
    address = models.CharField(verbose_name="direccion", max_length=60, blank=True, null=True)
    tel_req = models.CharField(verbose_name="telefono", max_length=20)
    tel_op = models.CharField(verbose_name="telefono2", max_length=20, blank=True, null=True)
    description = models.TextField(verbose_name="descripción", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de edición")
    location = models.ForeignKey(Location,verbose_name="localidad", on_delete=models.PROTECT)
    breed = models.ForeignKey(Breed, verbose_name="raza", blank=True, null=True, on_delete=models.SET_NULL)
    # pics = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
  


class Adoption(PetMixin):


    class Meta:
        verbose_name = "adopcion"
        verbose_name_plural = "adopciones"

    def __str__(self):
        return '%s - %s - %s' % (self.location, self.created.strftime('%x'), self.profile)



class Straying(PetMixin):

    date_lost = models.DateField(verbose_name="fecha Extravio", auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "extravio"
        verbose_name_plural = "extravios"

    def __str__(self):
        return '%s - %s' % (self.date_lost.strftime('%x'), self.profile)

class Finding(PetMixin):

    date_find = models.DateField(verbose_name="fecha Hallazgo", auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "hallazgo"
        verbose_name_plural = "hallazgos"

    def __str__(self):
        return '%s - %s' % (self.date_find.strftime('%x'), self.profile)    


class Cross(PetMixin):


    class Meta:
        verbose_name = "cruza"
        verbose_name_plural = "cruzas"

    def __str__(self):
        return '%s - %s' % (self.breed, self.profile)

class PostMixin(models.Model):

    class Meta:
        abstract = True
    
    title = models.CharField(verbose_name="titulo", max_length=60)
    address = models.CharField(verbose_name="direccion", max_length=60)
    description = models.TextField(verbose_name="descripción", null=True, blank=True)
    tel_req = models.CharField(verbose_name="telefono", max_length=20)
    tel_op = models.CharField(verbose_name="telefono2", max_length=20, blank=True, null=True)
    web = models.URLField(verbose_name="web",max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de edición")
    location = models.ForeignKey(Location,verbose_name="localidad", on_delete=models.PROTECT)

class Trainer(PostMixin):

    profile = models.OneToOneField(Profile, verbose_name="perfil", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "adiestrador"
        verbose_name_plural = "adiestradores"

    def __str__(self):
        return '%s - %s - %s - %s' % ( self.created.strftime('%x'), self.location, self.profile, self.title)

class Ad(PostMixin):

    profile = models.ForeignKey(Profile, verbose_name="perfil", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "anuncio"
        verbose_name_plural = "anuncios"

    def __str__(self):
        return '%s - %s' % (self.title, self.profile)


