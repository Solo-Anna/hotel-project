# Generated by Django 4.1.1 on 2022-09-19 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_countryid_country_countryid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='countryId',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
    ]
