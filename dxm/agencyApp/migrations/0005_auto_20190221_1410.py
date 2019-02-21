# Generated by Django 2.1.5 on 2019-02-21 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agencyApp', '0004_auto_20190219_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='agencyinfo',
            name='color_code',
            field=models.CharField(default='', max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='testinfo',
            name='agencyno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agencyApp.AgencyInfo', verbose_name='销售商'),
        ),
    ]
