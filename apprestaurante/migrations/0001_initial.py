# Generated by Django 2.1.3 on 2018-11-22 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('nit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apprestaurante.Cliente')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apprestaurante.Empleado')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apprestaurante.Menu')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='plato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apprestaurante.Plato'),
        ),
    ]