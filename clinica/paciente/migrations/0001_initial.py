# Generated by Django 4.1.2 on 2022-11-01 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('dni', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.IntegerField()),
            ],
        ),
    ]