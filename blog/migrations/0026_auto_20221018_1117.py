# Generated by Django 3.2.5 on 2022-10-18 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_contactus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name_plural': 'Contact  Us'},
        ),
        migrations.AddField(
            model_name='contactus',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
