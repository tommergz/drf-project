# Generated by Django 4.0 on 2021-12-14 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('innotter', '0006_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=65),
        ),
    ]
