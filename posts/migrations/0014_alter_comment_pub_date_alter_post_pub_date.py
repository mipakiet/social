# Generated by Django 4.1.6 on 2023-02-19 14:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_alter_comment_pub_date_alter_post_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 19, 15, 28, 16, 109627)),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 19, 15, 28, 16, 108627)),
        ),
    ]