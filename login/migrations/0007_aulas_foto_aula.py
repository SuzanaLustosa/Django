# Generated by Django 2.2.6 on 2022-10-17 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_aulas_publicado'),
    ]

    operations = [
        migrations.AddField(
            model_name='aulas',
            name='foto_aula',
            field=models.ImageField(blank=True, upload_to='fotos/%d%m%Y/'),
        ),
    ]
