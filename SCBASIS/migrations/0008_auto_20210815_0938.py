# Generated by Django 3.1.3 on 2021-08-15 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SCBASIS', '0007_auto_20210815_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_description',
            field=models.FileField(upload_to='files/course_guides'),
        ),
    ]