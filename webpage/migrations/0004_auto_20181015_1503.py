# Generated by Django 2.1.2 on 2018-10-15 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0003_showcase_sub_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='content',
            field=models.TextField(),
        ),
    ]