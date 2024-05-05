# Generated by Django 5.0.3 on 2024-05-05 01:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AtaResultados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turma', models.CharField(max_length=100)),
                ('serie', models.CharField(max_length=50)),
                ('ano', models.IntegerField(max_length=4)),
                ('aluno', models.CharField(max_length=300)),
                ('nt_art', models.CharField(max_length=3, validators=[django.core.validators.RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='Arte')),
                ('nt_bio', models.CharField(max_length=3, validators=[django.core.validators.RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='Biologia')),
                ('nt_edf', models.CharField(max_length=3, validators=[django.core.validators.RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='Ed. Física')),
                ('nt_fil', models.CharField(max_length=3, validators=[django.core.validators.RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='Filosofia')),
                ('nt_fis', models.CharField(max_length=3, validators=[django.core.validators.RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='Física')),
                ('nt_geo', models.CharField(max_length=3, validators=[django.core.validators.RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='Geografia')),
                ('nt_his', models.CharField(max_length=3, validators=[django.core.validators.RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='História')),
                ('nt_lin', models.CharField(max_length=3, validators=[django.core.validators.RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='L. Inglesa')),
                ('nt_lpt', models.CharField(max_length=3, validators=[django.core.validators.RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='L. Portuguesa')),
                ('nt_mat', models.CharField(max_length=3, validators=[django.core.validators.RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='Matemática')),
                ('nt_pro', models.CharField(max_length=3, validators=[django.core.validators.RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='Projeto de Vida')),
                ('nt_qui', models.CharField(max_length=3, validators=[django.core.validators.RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='Química')),
                ('nt_soc', models.CharField(max_length=3, validators=[django.core.validators.RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='Sociologia')),
                ('nt_tec', models.CharField(max_length=3, validators=[django.core.validators.RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='Tecnologia')),
            ],
        ),
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
