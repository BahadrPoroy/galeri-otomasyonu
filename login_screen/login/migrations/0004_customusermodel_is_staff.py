# Generated by Django 3.2.5 on 2021-08-23 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_remove_customusermodel_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusermodel',
            name='is_staff',
            field=models.BooleanField(default=True, editable=False),
        ),
    ]
