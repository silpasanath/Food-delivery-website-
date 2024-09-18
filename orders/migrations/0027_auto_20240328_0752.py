# Generated by Django 2.2.7 on 2024-03-28 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0026_auto_20240327_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=1),
        ),
        migrations.AlterField(
            model_name='dominos',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='kapilavastu',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='malabar',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='nmr',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='omr',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pizzahut',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
