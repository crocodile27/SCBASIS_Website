# Generated by Django 3.1.3 on 2021-08-11 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SCBASIS', '0004_auto_20210811_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='recommendation_of_course',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='recommended_resources',
            field=models.CharField(default=None, max_length=2000, null=True),
        ),
    ]
