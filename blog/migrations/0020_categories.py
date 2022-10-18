# Generated by Django 3.2.5 on 2022-10-18 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_delete_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Scripture', 'Scripture'), ('Life', 'Life'), ('Health', 'Health'), ('Fashion', 'Fashion'), ('Beauty', 'Beauty')], max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='categories')),
            ],
        ),
    ]
