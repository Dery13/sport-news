# Generated by Django 4.1.4 on 2022-12-21 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_berita'),
    ]

    operations = [
        migrations.AddField(
            model_name='berita',
            name='conten',
            field=models.TextField(blank=True, null=True),
        ),
    ]