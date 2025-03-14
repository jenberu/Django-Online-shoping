# Generated by Django 5.0.6 on 2024-10-14 13:26

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_alter_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='shop_logos/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='name', unique=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='name', unique=True),
        ),
    ]
