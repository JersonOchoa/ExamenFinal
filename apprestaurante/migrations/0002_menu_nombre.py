# Generated by Django 2.1.3 on 2018-11-22 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apprestaurante', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='nombre',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]