# Generated by Django 5.0.6 on 2024-07-10 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_shop_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRecommandation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('purchased_with_product_id', models.IntegerField()),
                ('purchased_with_times', models.IntegerField(default=0)),
            ],
        ),
    ]
