# Generated by Django 4.1.1 on 2022-09-30 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_rename_image_category_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Image',
            new_name='image',
        ),
    ]
