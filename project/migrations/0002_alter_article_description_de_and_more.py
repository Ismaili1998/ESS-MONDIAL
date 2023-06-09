# Generated by Django 4.1.7 on 2023-07-05 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description_de',
            field=models.TextField(max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='description_en',
            field=models.TextField(max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='description_fr',
            field=models.TextField(max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='client_ref',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
