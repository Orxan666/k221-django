# Generated by Django 4.2.2 on 2023-07-01 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
