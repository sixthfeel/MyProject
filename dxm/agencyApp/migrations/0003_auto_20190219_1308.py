# Generated by Django 2.1.5 on 2019-02-19 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agencyApp', '0002_agencyinfo_agencyonprd'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testinfo',
            old_name='testappl_date',
            new_name='testappldate',
        ),
        migrations.RenameField(
            model_name='testinfo',
            old_name='testend_date',
            new_name='testenddate',
        ),
        migrations.RenameField(
            model_name='testinfo',
            old_name='teststart_date',
            new_name='teststartdate',
        ),
    ]