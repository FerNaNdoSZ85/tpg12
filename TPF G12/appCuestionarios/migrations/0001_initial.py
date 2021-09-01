# Generated by Django 3.2.6 on 2021-08-29 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=120)),
                ('numero_de_preguntas', models.IntegerField()),
                ('tiempo', models.IntegerField(help_text='Duración del cuestionario en minutos')),
                ('dificultad', models.CharField(choices=[('Fácil', 'Fácil'), ('Medio', 'Medio'), ('Difícil', 'Difícil')], max_length=7)),
            ],
            options={
                'verbose_name_plural': 'Cuestionarios',
            },
        ),
    ]
