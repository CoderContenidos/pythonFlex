# Generated by Django 4.2.5 on 2023-09-23 07:33

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peluche', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelucheanimal',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='pelucheanimal',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='peluches'),
        ),
    ]