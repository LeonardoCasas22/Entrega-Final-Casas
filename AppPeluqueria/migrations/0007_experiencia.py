# Generated by Django 4.0.5 on 2022-07-18 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPeluqueria', '0006_rename_apellido_contacto_apellido_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('tratamiento', models.CharField(max_length=40)),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=4000)),
                ('imagen', models.ImageField(null=True, upload_to='experiencias')),
            ],
        ),
    ]
