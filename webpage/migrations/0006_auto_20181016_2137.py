# Generated by Django 2.1.2 on 2018-10-17 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0005_auto_20181016_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='content',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='home',
            name='name',
            field=models.CharField(default=True, max_length=200),
            preserve_default=False,
        ),
    ]
