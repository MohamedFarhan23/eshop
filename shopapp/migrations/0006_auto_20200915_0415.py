# Generated by Django 3.0.8 on 2020-09-15 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0005_category_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='pro_image',
        ),
        migrations.AddField(
            model_name='category',
            name='cat_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='category',
            name='rate',
            field=models.FloatField(null=True),
        ),
    ]
