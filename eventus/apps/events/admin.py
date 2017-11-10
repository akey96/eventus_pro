# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category,Event,Assistant,Comments

admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Assistant)
admin.site.register(Comments)

# Register your models here.
