# Generated by Django 5.2 on 2025-05-11 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_category_rename_descriptopn_menu_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='categories/default.jpg', upload_to='categories/'),
        ),
    ]
