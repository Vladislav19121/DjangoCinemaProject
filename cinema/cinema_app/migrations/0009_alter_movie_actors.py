# Generated by Django 5.1.4 on 2025-01-27 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0008_alter_actor_image_alter_director_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', to='cinema_app.actor'),
        ),
    ]
