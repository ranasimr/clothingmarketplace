# Generated by Django 5.0.3 on 2024-04-21 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_address_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={},
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(default='N/A', max_length=50),
        ),
    ]
