# Generated by Django 4.1.7 on 2023-02-27 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('First_name', models.CharField(max_length=32)),
                ('Middle_name', models.CharField(max_length=32)),
                ('Last_name', models.CharField(max_length=32)),
                ('user_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('OT', 'Others')], max_length=32)),
                ('Age', models.IntegerField()),
                ('Phone', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
    ]
