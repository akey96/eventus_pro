# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
"""este archivo contiene los modelos para esta app"""

#, fijarse las configuraiones que hicimos en el settings.base.py  para q funciones este User personalizado


# creamos un Manager para estos User, esto nos sirve para crear usuarios comunes y superusuario
# puesto q solo en el modelo User definimos los atributo que este tendra, mas nos, si este podra ser
#super usuario o un usuario comun, tambien validaremos q meta datos correcto, puesto que este modelo
# es el mas importante de todos, porq este maneja las cuentas de el sistemas
#heredamos de estas dos Clases para que crear ese clase
class UserManager(BaseUserManager,models.Manager):

    # esta funcion lo que hara es validaar todos los datos de los usuarios ,q pasemos cuando vallamos a crear un usuario o
    #super usuario, recibe como parametros:
        #username,email,password,is_staff,is_superuser y otros
    def _create_user(self,username,email,password,is_staff,is_superuser,**extra_fields):
        # creamos una variables donde pasamos nuestro el dominio de nuestro email a minusculas
        email = self.normalize_email(email)
        #valida si no ingreso un email, si no ingreso levanta un error
        if not email:
            raise ValueError('El email debe ser obligatorio')
        # creamos una variable user donde guardaremos los datos pasados por parametros y tambien
        # agregamos los que creamos convenientes, tal como ser is_active,etc
        # esta variable nos sirve retornat todos los campos llendos del modelo User
        user = self.model(username=username,email=email,is_active=True,is_staff=is_staff,is_superuser=is_superuser,**extra_fields)

        #con este metodo seteamos el password q viene como parametro, para q asi asignar el password
        user.set_password(password)

        # guardamos estos datos usando esta base de datos
        user.save(using = self._db)

        #por ultimo retornamos la variable donde estan los datos del usuario
        return user

    # ahora creamos un funcion q va a crear un usuario comun
    def create_user(self,username, email, password=None,**extrafield):
        # aqui le pasamos todos lo argumentos que recaudamos a esta funcion, q es la q valida
        #todos los datos para crear un User
        return self._create_user(username,email,password,False,False,**extrafield)

    # ahora creamos un funcion q va a crear un super_usuario
    def create_superuser(self,username, email, password=None,**extrafield):
        # aqui le pasamos todos lo argumentos que recaudamos a esta funcion, q es la q valida
        #todos los datos para crear un supersuario, eslo mismo q el de arriba, sino q aqui
        #le pasamos q si va a poder acceder al site_admin(is_staff) y q es un superusuario(is_superuser)
        return self._create_user(username,email,password,True,True,**extrafield)



# Este es un modelo personalizado de User, es muy distinto al que nos presenta Django
# heredamos de estos dos Clases que nos trae Django
class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # este atributo almacenara una imagen del del usuario, en la cual le estamos diciendo q se almacene
    # en una carpeta llamada users, esta carpeta se creara en un directorio que definiremos despues
    avatar = models.ImageField(upload_to = 'users')     #falta hacer algo

    # en este atributo estamos un objecto de una clase q lo q hace es validar
    objects = UserManager()

    # este atributo almacenara si este usuario es activo, por defecto lo colocamos en True,
    #pero le podemos cambiar a False, cuenta de eliminar una usuario
    is_active = models.BooleanField(default=True)

    # este atributo almacenara si un Usuario tiene permiso para accede al a base de datos q nos
    # trae Djanfo, es decir al sitio del administrador, por defecto lo colocamos en False
    is_staff = models.BooleanField(default=False)

    # esto es para q un super usuario se puede loguear con el username de este modelo
    USERNAME_FIELD = 'username'
    # campos con los cuales se requiere para crear un super usuario, en este caso solo estamos
    # colocando el email
    REQUIRED_FIELDS = ['email']

    # sobre cargamos esta funcion que nos retornara el nombre del User
    def get_short_name(self):
        return self.username

