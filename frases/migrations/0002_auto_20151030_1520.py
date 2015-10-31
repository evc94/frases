# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frases', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='frase',
            old_name='created_date',
            new_name='fecha_creacion',
        ),
        migrations.RenameField(
            model_name='frase',
            old_name='published_date',
            new_name='fecha_publicacion',
        ),
    ]
