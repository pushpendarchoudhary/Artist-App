# Generated by Django 4.1.11 on 2023-09-30 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0004_alter_artist_works'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='works',
            field=models.ManyToManyField(related_name='artists', to='demoapp.work'),
        ),
    ]
