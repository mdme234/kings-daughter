# Generated by Django 3.2.5 on 2022-10-18 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20221018_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticles',
            name='articleCategory',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
