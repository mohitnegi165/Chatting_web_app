# Generated by Django 2.0 on 2018-07-10 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_auto_20180706_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phn_numb',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=' ', max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
