# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# importamo este metodo para que podamos usarlos en los atributos slug de los modelos
from django.template.defaultfilters import slugify


#importamo del settings que es paquete dond estan las configuraciones basicas
#dentro de este esta la variable la cual tiene la ruta del User personalizado(AUTH_USER_MODEL)
# para asi poder hacer usu de esta, cuando nos referimos al settings, es la variable
# q damos de al alta al momento de levantar el servidor (runserver --settings=setting.base....)
from django.conf import settings


#definimos un clase de un modelo q va heredar de models.Model que es la que va registrar las marcas
#de tiempo, tiene dos atributos: de creacion y modeificacion
class TimeStampModel(models.Model):

    #auto_now_add=True = registra la una hora y fecha apenas se instancie un objeto
    create = models.DateTimeField(auto_now_add=True)

    # auto_now=True = registra la una hora y fecha
    modified = models.DateTimeField(auto_now=True)

    # definimos una clase Meta que le indicamos q sera una clase abstracta, es decir que no se
    # va a crear una tabla en la base de datos, y q la vamos a heredar a futuros modelos
    class Meta:
        abstract = True


# definimos un Modelo Category q nos creara un objeto q almacenara las categorias de los eventos
class Category(models.Model):

    # nombre de la categoria
    name = models.CharField(max_length=50)

    # este campo hace referencia a almacenar una URL de la categoria
    # puesto q este tipo de campo hace referencia a caracteres especiales que se utilizan en las URL
    # agregamos este atributi editable=False   =  esto es para que no se pueda editar desde el administrador
    slug = models.SlugField(editable=False)

    # modificamos el metodo save q es el utilizamos cuando guardamos un registro de un objeto
    # a la BD

    def save(self,*args,**kwargs):

        if not self.id:
            # llena el atributo slug con el nombre de la categoria
            self.slug = slugify(self.name)

        # sobre cargamos el metodo super para q siga su camino y no haya inconvenientes
        super(Category,self).save(*args,**kwargs)

    # estamos retornando en nombre de la categoria
    def __str__(self):
        return self.name

# creamos este modelo q sera el pricipal de la app, que es la que guardara los datos de los eventos
# estamos heredando del modelo que creamos primeramente q es el TimeStampModel, que al heredar de este,
# estamos heredando indirectamente del modelo  models.Model y asi tambien los atributos de este,
# como ser el  create y modified
class Event(TimeStampModel):

    # atributo q almacenara el nombre del evento, y q es unico, es decir que no se puede repetir
    # este nombre en la BD
    name = models.CharField(max_length=200, unique = True)

    # este atributo almacenara las URL del evento
    slug = models.SlugField(editable=False)

    # este atributo almacenara un resumen de evento
    sumary = models.TextField(max_length=255)

    # este atributo almacenara el contenido del evento
    content = models.TextField()

    # este atributo almacenara una referencia al modelo Category, es decir es una llave foranea
    # uno a muchos
    category = models.ForeignKey(Category)

    # lugar en el cual se va a realizar el evento
    place = models.CharField(max_length=50)

    # este atributo almacenara la fecha de inicio del evento
    start = models.DateTimeField()

    # este atributo almacenara  la fecha en la cual acabara el evento
    finish= models.DateTimeField()

    # este atributo almacenara una imagen del evento, en la cual le estamos diciendo q se almacene
    # en una carpeta llamada events, esta carpeta se creara dentro en un directorio que
    #esta definida de la variable MEDIA_URL del archivo settings  ejemplo
    # proyecto_Dja.../eventus/media/events
    imagen = models.ImageField(upload_to = 'events')

    # este atributo almacenara si un evento es de paga o gratis, por defecto los colocamos
    # con valor True
    is_free = models.BooleanField(default=True)

    # este atributo almacenara  monto que llegara a costar el evento,
    # que tendra como maximo 5 digitos, 2 decimales y de valor por defecto de 0.00
    amount = models.DecimalField(max_digits=5,decimal_places=2,default=0.00)

    # este atributo almacenara el numero de personas que vieron este evento, y que no puede ser
    # un numero negativo, como valor por defecto 0
    view = models.PositiveIntegerField(default=0)

    # este atributo almacenara una referencia a un objeto del modelo User, a este Modelo lo creamos
    # en la app users,
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL)

    #sobre cargamos el metodo save q es el ejecutamos al momento de guardar un registro a la BD
    def save(self,*args,**kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Event,self).save(self,*args,**kwargs)

    def __str__(self):
        return self.name
# este Modelo es el que almacenara los datos de los usuario que asistiran a un evento
class Assistant(TimeStampModel):

    # este atributo almacenara una referencia a un objeto del modelo User, a este Modelo lo creamos
    # en la app users, es decir un user puede asistir a varios eventos
    assistant = models.ForeignKey(settings.AUTH_USER_MODEL)

    # este atributo almacenara una referencia los objetos del Modelo Event(ManyToMany),es decir:
    # un User puede asistir a varios Event, peso tambien un Event puede tener varios User
    event = models.ManyToManyField(Event)

    # este atributo almacenara si esque un este Assistend llego o no al evento por defecto esta en False
    attended = models.BooleanField(default=False)

    # este atributo almacenara  si es que este Asistente pago o no por este evento
    has_paid = models.BooleanField(default=False)

    def __str__(self):

        # retornamos el nombre del asistente y el nombre del evento
        return "%s %s" %(self.assistant.username, self.event.name)

class Comments(TimeStampModel):

    # este atributo almacenara una referencia a un objeto del modelo User, a este Modelo lo creamos
    # en la app users, es decir un user puede comentar varios  veces
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    # este atributo almacenara una referencia a un objeto del modelo Events, puesto que se tiene q saber
    # a que evento va referido el comentario
    event = models.ForeignKey(Event)

    # este atributo almacenara en contenido del comentario a realizar
    content = models.TextField()

    def __str__(self):
        # retornamos el nombre User que realizo el comentario y el nombre del evento
        return "%s %s" %(self.user.username, self.event.name)
