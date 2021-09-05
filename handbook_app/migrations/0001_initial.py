# Generated by Django 3.2.7 on 2021-09-03 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Handbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=255)),
                ('mini_title', models.CharField(blank=True, default='', max_length=255)),
                ('description', models.CharField(blank=True, default='', max_length=255)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='handbook_app.version')),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='code', max_length=255)),
                ('value', models.CharField(default='value', max_length=255)),
                ('handbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='handbook_app.handbook')),
            ],
        ),
    ]
