# Generated by Django 4.1.4 on 2022-12-21 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_berita_conten'),
    ]

    operations = [
        migrations.AlterField(
            model_name='berita',
            name='tanggal',
            field=models.CharField(max_length=100),
        ),
    ]
