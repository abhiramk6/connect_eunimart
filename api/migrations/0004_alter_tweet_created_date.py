# Generated by Django 4.1.7 on 2023-02-28 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_user_idd_tweet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]