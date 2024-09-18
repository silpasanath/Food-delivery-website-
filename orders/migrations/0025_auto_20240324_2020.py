# Generated by Django 2.2.7 on 2024-03-24 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0024_hotels'),
    ]

    operations = [
        migrations.CreateModel(
            name='Malabar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=200)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('img', models.CharField(default='/orders/images/salads/avocado.jpg', max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='SicilianPizza',
            new_name='Dominos',
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='Hotel',
        ),
        migrations.RenameModel(
            old_name='Salad',
            new_name='Kapilavastu',
        ),
        migrations.RenameModel(
            old_name='Pasta',
            new_name='NMR',
        ),
        migrations.RenameModel(
            old_name='Sub',
            new_name='OMR',
        ),
        migrations.RenameModel(
            old_name='RegularPizza',
            new_name='PizzaHut',
        ),
        migrations.DeleteModel(
            name='DinnerPlatters',
        ),
        migrations.DeleteModel(
            name='Hotels',
        ),
    ]
