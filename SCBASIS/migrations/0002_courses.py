# Generated by Django 3.1.3 on 2021-08-06 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SCBASIS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_course', models.CharField(max_length=32)),
                ('course_description', models.CharField(max_length=6000)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('course_category', models.CharField(max_length=50)),
                ('url_of_image', models.CharField(max_length=800)),
                ('viewable', models.BooleanField(blank=True, default=True, null=True)),
                ('editor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]