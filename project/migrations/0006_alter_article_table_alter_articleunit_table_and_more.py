# Generated by Django 4.1.7 on 2023-07-10 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_alter_supplier_supplier_nbr'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='article',
            table='Article',
        ),
        migrations.AlterModelTable(
            name='articleunit',
            table='Article_unit',
        ),
        migrations.AlterModelTable(
            name='buyer',
            table='Buyer',
        ),
        migrations.AlterModelTable(
            name='client_contact',
            table='Client_contact',
        ),
        migrations.AlterModelTable(
            name='commercialoffer',
            table='Commercial_offer',
        ),
        migrations.AlterModelTable(
            name='destination',
            table='Destination',
        ),
        migrations.AlterModelTable(
            name='file',
            table='File',
        ),
        migrations.AlterModelTable(
            name='project',
            table='Project',
        ),
        migrations.AlterModelTable(
            name='quoterequest',
            table='QuoteRequest',
        ),
        migrations.AlterModelTable(
            name='supplier',
            table='Supplier',
        ),
        migrations.AlterModelTable(
            name='supplier_contact',
            table='Supplier_contact',
        ),
        migrations.AlterModelTable(
            name='timeunit',
            table='Time_unit',
        ),
    ]
