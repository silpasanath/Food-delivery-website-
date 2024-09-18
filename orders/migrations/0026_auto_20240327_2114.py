# Generated by Django 2.2.7 on 2024-03-27 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0025_auto_20240324_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='dominos',
            name='rating',
            field=models.PositiveIntegerField(default=0, max_length=5),
        ),
        migrations.AddField(
            model_name='kapilavastu',
            name='rating',
            field=models.PositiveIntegerField(default=0, max_length=5),
        ),
        migrations.AddField(
            model_name='malabar',
            name='rating',
            field=models.PositiveIntegerField(default=0, max_length=5),
        ),
        migrations.AddField(
            model_name='nmr',
            name='rating',
            field=models.PositiveIntegerField(default=0, max_length=5),
        ),
        migrations.AddField(
            model_name='omr',
            name='rating',
            field=models.PositiveIntegerField(default=0, max_length=5),
        ),
        migrations.AddField(
            model_name='pizzahut',
            name='rating',
            field=models.PositiveIntegerField(default=0, max_length=5),
        ),
        migrations.AlterField(
            model_name='dominos',
            name='img',
            field=models.CharField(default='/orders/images/dominos/morocco_pizza.jpg', max_length=200),
        ),
        migrations.AlterField(
            model_name='kapilavastu',
            name='img',
            field=models.CharField(default='/orders/images/kapilavastu/avocado.jpg', max_length=200),
        ),
        migrations.AlterField(
            model_name='malabar',
            name='img',
            field=models.CharField(default='/orders/images/malabar/avocado.jpg', max_length=200),
        ),
        migrations.AlterField(
            model_name='omr',
            name='img',
            field=models.CharField(default='/orders/images/omr/sausage.jpg', max_length=200),
        ),
        migrations.AlterField(
            model_name='pizzahut',
            name='img',
            field=models.CharField(default='/orders/images/pizzahut/burger_pizza.jpg', max_length=200),
        ),
    ]
