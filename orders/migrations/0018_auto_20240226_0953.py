# Generated by Django 2.2.7 on 2024-02-26 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_pasta_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='dinnerplatters',
            name='img',
            field=models.CharField(default='/orders/images/platters/momos.jpg', max_length=200),
        ),
        migrations.AddField(
            model_name='regularpizza',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='sub',
            name='img',
            field=models.CharField(default='/orders/images/subs/sausage.jpg', max_length=200),
        ),
        migrations.AlterField(
            model_name='salad',
            name='img',
            field=models.CharField(default='/orders/images/salads/avocado.jpg', max_length=200),
        ),
    ]
