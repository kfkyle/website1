# Generated by Django 2.1.2 on 2018-10-15 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0002_about_more_services_servicesheader'),
    ]

    operations = [
        migrations.AddField(
            model_name='showcase',
            name='sub_title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]