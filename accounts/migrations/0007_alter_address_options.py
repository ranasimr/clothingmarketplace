# Generated by Django 5.0.3 on 2024-04-20 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_userprofile_address_line_3_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'permissions': [('can_delete_address', 'Can delete address')]},
        ),
    ]
