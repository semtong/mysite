# Generated by Django 2.0.4 on 2018-06-03 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0004_auto_20180603_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='updateDate',
            field=models.DateTimeField(null=True),
        ),
    ]
