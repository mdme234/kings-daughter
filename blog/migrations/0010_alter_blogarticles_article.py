# Generated by Django 3.2.5 on 2022-10-10 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_blogarticles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticles',
            name='article',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
    ]
