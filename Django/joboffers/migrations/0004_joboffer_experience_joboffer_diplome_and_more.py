# Generated by Django 4.1.7 on 2023-05-08 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joboffers', '0003_joboffer_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='joboffer',
            name='Experience',
            field=models.CharField(default='empty', max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='joboffer',
            name='diplome',
            field=models.CharField(default='empty', max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='joboffer',
            name='type_poste',
            field=models.CharField(default='empty', max_length=45),
            preserve_default=False,
        ),
    ]
