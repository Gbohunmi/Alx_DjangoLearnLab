# Generated by Django 5.1.6 on 2025-03-20 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='post',
            field=models.ManyToManyField(related_name='tag', to='blog.post'),
        ),
    ]
