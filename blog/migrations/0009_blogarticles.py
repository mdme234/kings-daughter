# Generated by Django 3.2.5 on 2022-10-10 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_subscribers'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogArticles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('ArticleImage', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('author', models.CharField(blank=True, max_length=200, null=True)),
                ('AuthorImage', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('article', models.TextField(blank=True, max_length=200, null=True)),
                ('ArticleImage1', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('ArticleImage2', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('ArticleImage3', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Blog  Articles',
            },
        ),
    ]
