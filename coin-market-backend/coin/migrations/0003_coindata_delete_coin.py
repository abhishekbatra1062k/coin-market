# Generated by Django 5.0.6 on 2024-05-13 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0002_alter_coin_circulating_supply_alter_coin_market_cap_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoinData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('symbol', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('one_hour_change', models.CharField(max_length=255)),
                ('twenty_four_hour_change', models.CharField(max_length=255)),
                ('seven_day_change', models.CharField(max_length=255)),
                ('market_cap', models.CharField(max_length=255)),
                ('volume_24h', models.CharField(max_length=255)),
                ('circulating_supply', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Coin',
        ),
    ]
