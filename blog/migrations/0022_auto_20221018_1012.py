# Generated by Django 3.2.5 on 2022-10-18 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_alter_blogarticles_articlecategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro_text', models.CharField(blank=True, max_length=500, null=True)),
                ('goal', models.CharField(blank=True, max_length=500, null=True)),
                ('pargraph_1', models.TextField(blank=True, max_length=1000, null=True)),
                ('pargraph_2', models.TextField(blank=True, max_length=200, null=True)),
                ('pargraph_3', models.TextField(blank=True, max_length=200, null=True)),
                ('pargraph_4', models.TextField(blank=True, max_length=200, null=True)),
                ('Image1', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('Image2', models.ImageField(blank=True, null=True, upload_to='blog')),
            ],
            options={
                'verbose_name_plural': 'About Us',
            },
        ),
        migrations.CreateModel(
            name='BlogAim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Indexer', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='about')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Aim  of  Blog',
            },
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
