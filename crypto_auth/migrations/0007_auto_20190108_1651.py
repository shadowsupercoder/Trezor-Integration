# Generated by Django 2.1.5 on 2019-01-08 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_auth', '0006_siteconfiguration_network_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdraw',
            name='status',
            field=models.CharField(choices=[('Pending', 'PENDING'), ('Rejected', 'REJECTED'), ('Success', 'SUCCESS')], default='Pending', help_text='Status', max_length=10),
        ),
        migrations.AlterField(
            model_name='withdraw',
            name='tx_hash',
            field=models.CharField(blank=True, help_text='Transaction hash', max_length=150),
        ),
    ]
