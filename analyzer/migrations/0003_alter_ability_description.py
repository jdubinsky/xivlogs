# Generated by Django 4.1.4 on 2023-01-03 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0002_alter_ability_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ability',
            name='description',
            field=models.CharField(max_length=1024),
        ),
    ]
