# Generated by Django 3.2.5 on 2022-10-18 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_alter_blogarticles_articlecategory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Categories',
        ),
    ]
