# Generated by Django 3.0 on 2020-01-13 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escBackend', '0002_auto_20200113_0315'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='Context',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
    ]
