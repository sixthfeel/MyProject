# Generated by Django 2.1.5 on 2019-02-19 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agencyApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agencyinfo',
            name='agencyonprd',
            field=models.CharField(default='', max_length=2),
            preserve_default=False,
        ),
    ]
